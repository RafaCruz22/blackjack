from lib2to3.pgen2.token import EQUAL
import random
from turtle import clear
from deckOfCards import Deck
from gameUI import UserInterface

class BlackJackEngine:
    def __init__(self):
        self.deck = Deck()
        self.UI = UserInterface()
        self.stats = Statistics()
        self.sumMin, self.sumCap = 12, 21 
        self.dealerScore, self.playerScore  = 0, 0
        self.dealersHand, self.playersHand = [], []
        self.round = 0

    def start(self):

        self.UI.banner("top", self.UI.gameIntro())

        newGame = self.UI.startDialog()
        if newGame == True:
            self.deck.shuffleDeck()
            self.playRound()
        
        self.showStats()
 
    def playRound(self):
        while True:
            self.shuffle()

            #deals cards to player first then dealer. alternating cards dealt
            self.firstServe()

            deckCount = self.deck.getDeckCount()

            self.round += 1

            self.UI.banner("round", str(self.round))
            self.UI.banner("deck",None)
            self.UI.deckCard(deckCount)
            self.UI.banner("card", None)
            
            self.showHands("hideDealer")

            #checks if player was dealt a hand over 21 
            self.check("dealt_over_21") 

            if self.calculatesHand() == False:
                return False

    def shuffle(self):
        if self.round%3 == 0 and self.round >= 1:
            self.deck.resetDeck()
            for i in range(3):
                self.deck.shuffleDeck()    
            self.UI.banner("complete","--> Shuffle Successful <--")

    def firstServe(self):
        turn = "players"
        for dealCard in range(4):
            suit, rank = self.deck.dealCard()

            if turn == "players":
                self.playersHand.append((rank, suit))
                self.playerScore += rank
                turn = "dealer"
            else: 
                self.dealersHand.append((rank, suit))
                self.dealerScore += rank
                turn = "players"
    
    def calculatesHand(self):
        while self.playerScore != 0:
            match self.UI.playerDecision():
                #player hit
                case "hit":
                    # might want to display CARD
                    suit, rank = self.deck.dealCard()
                    self.playersHand.append((rank, suit))
                    self.playerScore += rank
                    self.showHands("hideDealer")
                    self.check("over_21")
                    
                
                #player Stayed
                case "stay":
                    # deal to dealer until dealers has over players hand,at 21, or over the limit
                    # if dealer & players score are eqaul player keeps his bet
                    while self.check("dealerWon") != False: 
                        suit, rank = self.deck.dealCard()
                        self.dealersHand.append((rank, suit))
                        self.dealerScore += rank

                    break
                
                case "doubledown":
                    pass

                #player wants to quit game
                case _:
                    quitResult = self.UI.quitDialog()
                    
                    match quitResult: 
                        case True:
                            return True
                            self.deck.resetDeck()
                        case False: 
                            return False 
                        
                        case _: 
                            quitResult        

    def showHands(self,show):
        print()
        match show:
            case "both":
                self.viewDealer(None)
                self.UI.displayScore(self.dealerScore)
                print()

                self.viewPlayer()
                print()
            
            case "hideDealer":
                self.viewDealer("hide")
                print()

                self.viewPlayer()
                print()

            case _:
                print("Error")

    def viewDealer(self, hide):
        self.UI.whosTurn("Dealer")
        self.UI.createCard(self.dealersHand)
        self.UI.displayCard(len(self.dealersHand), hide)
        self.UI.resetCards()

    def viewPlayer(self): 
        self.UI.whosTurn("Player")
        self.UI.createCard(self.playersHand)
        self.UI.displayCard(len(self.playersHand), None)
        self.UI.displayScore(self.playerScore)
        self.UI.resetCards()
        print()

    def check(self, check):
        dealerWins = self.dealerScore > self.playerScore
        dealerBust = self.dealerScore > self.sumCap
        playerBust = self.playerScore > self.sumCap
        dealer21 = self.dealerScore == self.sumCap
        player21 = self.playerScore == self.sumCap
        
        match check:
            case "dealt_over_21":
                if playerBust:
                    self.showHands("both")
                    self.UI.displayWinner("dealt_lost", None)
                    self.stats.increaseRound()
                    self.resetHands()
                    
                    return False
            
            case "over_21":
                if playerBust:
                    self.showHands("both")
                    self.UI.displayWinner("over_21", None)
                    self.stats.increaseRound()
                    self.resetHands()
                    
                    return False
                
                elif player21:
                    self.playerWon()
                    return False

            case "dealerWon":
                # not sure if equal who wins or nothing happens. temp: dealer must be strictly over player
                if (dealerWins | dealer21) and (dealerBust is False):
                    self.dealerWon()
                    return False  

                elif dealerBust:
                    self.playerWon()
                    return False
            
            case _: 
                print("No Match Found.")

    def playerWon(self): 
        self.showHands("both")
        self.UI.displayWinner("you_won", self.playerScore)
        self.stats.increaseRound()
        self.resetHands()

    def dealerWon(self): 
        self.showHands("both")
        self.UI.displayWinner("dealerWon", None)
        self.stats.increaseRound()
        self.resetHands()

    def resetHands(self): 
        self.dealersHand, self.playersHand = [], []
        self.dealerScore, self.playerScore  = 0, 0

    def showStats(self):
        scores = self.stats.getScore()
        rounds = self.stats.getRoundsPlayed(self.round)
        percentage = self.stats.average()
        self.UI.gameStats(scores, rounds, percentage)

class Statistics:
    def __init__(self):
        self.allScores = 0
        self.allRoundsPlayed = 0
        self.numOfRounds = 0

    def getScore(self):
        return self.allScores

    def playerPoints(self, endScore):
        self.allScores += endScore

    def increaseRound(self):
        self.numOfRounds += 1

    def getRoundsPlayed(self, rounds):
        self.allRoundsPlayed += rounds
        return self.allRoundsPlayed

    def average(self):
        try: 
            avg = self.allScores / self.numOfScores
            return avg
        
        except: 
            return 0

if __name__ == "__main__":
    test = BlackJackEngine()
    test.start()
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

        newGame = self.UI.playNewGame()
        if newGame == True:
            self.playRound()
        
        self.showStats()
 
    def playRound(self):
        while self.deck.getDeckCount() > 1:

            self.round += 1

            self.UI.banner("round", str(self.round))
            self.UI.banner("deck", str(self.deck.getDeckCount()))
            self.UI.banner("card", None)

            #deals a card to player first then dealer. cards dealt alternating
            self.dealHand()
            self.showHands("hideDealer")

            #checks if player was dealt a hand over 21 
            self.check("dealt_over_21") 

            if self.calculatesHand() == False:
                return False

    def dealHand(self):
        turn = "players"
        for dealCards in range(4):
            suit, rank = self.deck.dealCards()

            if turn == "players":
                self.playersHand.append([rank, suit])
                self.playerScore += rank
                turn = "dealer"
            else: 
                self.dealersHand.append([rank, suit])
                self.dealerScore += rank
                turn = "players"
    
            self.deck.decreaseMainDeck()

    def calculatesHand(self):
        
        while self.playerScore != 0:
            
            stayHit = self.UI.stayHit()

            if stayHit != False:
                self.UI.banner("deck", str(self.deck.getDeckCount()))
            
            #player hit
            if stayHit == "hit":
                # might want to display CARD
                suit, rank = self.deck.dealCards()
                self.playersHand.append([rank, suit])

                self.deck.decreaseMainDeck()
                self.playerScore += rank

                self.showHands("hideDealer")
                
                self.check("hit_one_card_remain")
                check = self.check("over_21")
                
                if check == "end":
                    break
            
            #player Stayed
            elif stayHit == "stay":

                # deal to dealer until dealers has over players hand,at 21, or over the limit
                # if dealer & players score are eqaul player keeps his bet
                check = self.check("dealerWon") 
                
                if check == "end":
                    break
            
            elif stayHit == False:
                quitResult = self.UI.quitGameDialog()
                
                match quitResult: 
                    case True:
                        return True
                    case False: 
                        return False 
                    
                    case _: 
                        quitResult        

    def showHands(self,show):
        print()
        match show:
            case "both":
                self.UI.whosTurn("Dealer")
                self.UI.createCard(self.dealersHand,None)
                self.UI.displayScore(self.dealerScore)
                print()

                self.UI.whosTurn("Player")
                self.UI.createCard(self.playersHand,None)
                self.UI.displayScore(self.playerScore)
                print()
            
            case "hideDealer":
                self.UI.whosTurn("Dealer")
                self.UI.createCard(self.dealersHand,"hide")
                print()

                self.UI.whosTurn("Player")
                self.UI.createCard(self.playersHand,None)
                self.UI.displayScore(self.playerScore)
                print()

            case _:
                print("Error")

    def check(self, check):
        match check:
            case "dealt_over_21":
                if self.playerScore > self.sumCap:
                    self.UI.banner("card", None)
                    self.showHands("both")

                    self.UI.displayWinner("dealt_lost", None)
                    self.stats.increaseRound()

                    self.playerScore = 0
                    self.resetHands()
            
            case "hit_one_card_remain":
                if self.deck.getDeckCount() <= 1:
                    if (self.playerScore <= self.sumCap) and (self.playerScore > self.dealerScore):
                        self.stats.playerPoints(self.playerScore)

                        self.showHands("both")

                        self.UI.displayWinner("you_won", self.playerScore)
                        self.stats.increaseRound()
                        

                        self.resetHands()
            
            case "over_21":
                if self.playerScore > self.sumCap:
                    
                    self.showHands("both")
                    self.UI.displayWinner("over_21", None)
                    self.stats.increaseRound()

                    self.resetHands()
                    return "end"
        
            case "dealerWon":
                if self.playerScore <= self.dealerScore and self.dealerScore <= self.sumCap:
                    
                    self.showHands("both")

                    self.UI.displayWinner("dealerWon", None)
                    self.stats.increaseRound()

                    self.resetHands()
                    
                else:
                    self.showHands("both")

                    self.UI.displayWinner("you_won", self.playerScore)
                    self.stats.playerPoints(self.playerScore)
                    self.stats.increaseRound()

                    self.resetHands()
                    return "end"
    
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
import random
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

        self.UI.banner("simpleLine", None)
        print()
        self.UI.gameIntro()
        print()
        self.UI.banner("simpleLine", None)

        deck = self.deck.getDeckCount()
        print()
        self.UI.displayCard("deck", None, deck)
        
        newGame = self.UI.playNewGame()
        if newGame == True:
            self.playRound()
        
        scores = self.stats.getScore()
        rounds = self.stats.getRoundsPlayed(self.round)
        percentage = self.stats.average()
        self.UI.gameStats("beforeStart", scores, rounds, percentage)

    def playRound(self):
        print()
        
        while self.deck.getDeckCount() > 1:

            self.round += 1

            print()
            self.UI.banner("simpleLine", None)
            self.UI.headingPrint(self.round)

             #dealers hand
            self.UI.whomsTurn("Dealer's")
            for deal in range(2):
                randSuit, cardValue = self.deck.dealCards()
                self.dealersHand.append([cardValue, randSuit])
                self.deck.decreaseMainDeck()
                self.dealerScore += cardValue
            
            self.UI.displayCards(self.dealersHand)
            # self.UI.displayScore(self.dealerScore)
            print()

            #players hand
            self.UI.whomsTurn("Player's")
            for deal in range(2):
                randSuit, cardValue = self.deck.dealCards()
                self.playersHand.append([cardValue, randSuit])
                self.deck.decreaseMainDeck()
                self.playerScore += cardValue

            self.UI.displayCards(self.playersHand)
            self.UI.displayScore(self.playerScore)
            print()

            self.UI.displayScore(self.handSum)
            self.UI.banner("simpleLine", None)
            print()

            self.check("dealt_over_21")
            
            while self.handSum != 0:
                check = self.check("empty")
                
                if check == "end":
                    break
                
                deck = self.deck.getDeckCount()
                self.UI.displayCard("deck", None, deck)
                stayHit = self.UI.stayHit()
                
                if stayHit == "hit":
                    self.UI.displayCard("hit card", None, None)
                    randSuit, cardValue = self.deck.dealCards()
                    self.dealersHand.append([cardValue, randSuit])
                    self.UI.displayCards(self.dealersHand)
                    self.deck.decreaseMainDeck()
                    self.handSum += cardValue
                    
                    self.UI.displayScore(self.handSum)
                    self.check("hit_one_card_remain")
                    check = self.check("over_21")

                    print("it", check)
                    
                    if check == "end":
                        break
                
                elif stayHit == "stay":
                    check = self.check("under_12")
                    
                    if check == "end":
                        break
                
                elif stayHit == False:
                    quitResult = self.UI.quitGameDialog()
                 
                    match quitResult: 
                        case True:
                            continue 
                        case False: 
                            return False 
                        
                        case _: 
                            quitResult

        # scores = self.stats.getScore()
        # rounds = self.stats.getRoundsPlayed(self.round)
        # percentage = self.stats.average()
        # self.UI.gameStats(None,scores, rounds, percentage)
        return False

    def check(self, checks):
        if checks == "empty":
            if self.deck.getDeckCount() == 0:
                if (self.handSum <= self.sumCap) and (self.handSum >= self.sumMin):
                    self.stats.addScores(self.handSum)
                    self.UI.winLoseDisplay("you_won")
                    self.stats.increaseNumOfScore()
                    self.handSum = 0
                
                elif self.handSum < self.sumMin:
                    self.UI.winLoseDisplay(None, "under_12", None)
                    self.stats.increaseNumOfScore()
                    self.handSum = 0
                self.UI.deckDisplay("emtpy")
                return "end"
        
        if checks == "dealt_over_21":
            if self.handSum > self.sumCap:
                self.UI.winLoseDisplay(None, "dealt_lost", None)
                self.stats.increaseNumOfScore()
                self.handSum = 0
                self.resetHands()
        
        if checks == "hit_one_card_remain":
            if self.deck.getDeckCount() <= 1:
                if (self.handSum <= self.sumCap) and (self.handSum >= self.sumMin):
                    self.stats.addScores(self.handSum)
                    self.UI.winLoseDisplay("you_won", None, self.handSum)
                    self.stats.increaseNumOfScore()
                    self.handSum = 0
        
        if checks == "over_21":
            if self.handSum > self.sumCap:
                self.UI.winLoseDisplay(None, "over_21", None)
                self.stats.increaseNumOfScore()
                self.handSum = 0
                self.resetHands()

                return "end"
       
        if checks == "under_12":
            if self.handSum < self.sumMin:
                self.UI.winLoseDisplay(None, "under_12", None)
                self.stats.increaseNumOfScore()
                self.handSum = 0
                self.resetHands()
                
            else:
                self.stats.addScores(self.handSum)
                self.UI.winLoseDisplay("you_won", None, self.handSum)
                self.stats.increaseNumOfScore()
                self.handSum = 0
                self.resetHands()

                return "end"
    
    def resetHands(self): 
        self.dealersHand = []

class Statistics:
    def __init__(self):
        self.allScores = 0
        self.allRoundsPlayed = 0
        self.numOfScores = 0

    def getScore(self):
        return self.allScores

    def addScores(self, endScore):
        self.allScores += endScore

    def increaseNumOfScore(self):
        self.numOfScores += 1

    def getRoundsPlayed(self, rounds):
        self.allRoundsPlayed += rounds
        return self.allRoundsPlayed

    def average(self):
        try: 
            avg = self.allScores / self.numOfScores
            return avg
        
        except: 
            return 0

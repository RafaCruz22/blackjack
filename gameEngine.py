import random
import deckCards
import gameUI

class BlackJackGame:
    def __init__(self):
        self.deck = deckCards.Deck()
        self.UI = gameUI.UserInterface()
        self.stats = Statistics()
        self.sumCap = 21
        self.sumMin = 12
        self.handSum = 0
        self.numHand = 0

    def playGame(self):

        self.UI.banner("simpleLine", None)
        print()
        self.UI.gameIntro()
        print()
        self.UI.banner("simpleLine", None)

        deck = self.deck.getMainDeck()
        print()
        self.UI.displayCard("deck", None, deck)
        
        newGame = self.UI.playNewGame()
        if newGame == True:
            self.playRound()
        
        scores = self.stats.getScore()
        rounds = self.stats.getRoundsPlayed(self.numHand)
        percentage = self.stats.average()
        self.UI.endGame("beforeStart", scores, rounds, percentage)

    def playRound(self):
        print()
        while self.deck.getMainDeck() > 1:

            self.numHand += 1

            print()
            self.UI.banner("simpleLine", None)
            self.UI.headingPrint(self.numHand)

            for firstDeal in range(2):
                randSuit, cardValue = self.deck.dealCards()
                self.UI.displayCard("deal card", randSuit, cardValue)
                self.deck.decreaseMainDeck()
                self.handSum += cardValue
            
            self.UI.displayScore(self.handSum)
            self.UI.banner("simpleLine", None)
            print()

            self.check("dealt_over_21")
            
            while self.handSum != 0:
                check = self.check("empty")
                
                if check == "end":
                    break
                
                deck = self.deck.getMainDeck()
                self.UI.displayCard("deck", None, deck)
                stayHit = self.UI.stayHit()
                
                if stayHit == "hit":
                    self.UI.displayCard("hit card", None, None)
                    randSuit, cardValue = self.deck.dealCards()
                    self.UI.displayCard("deal card", randSuit, cardValue)
                    self.deck.decreaseMainDeck()
                    self.handSum += cardValue
                    self.UI.displayScore(self.handSum)
                    self.check("hit_one_card_remain")
                    check = self.check("over_21")
                    
                    if check == "end":
                        break
                
                elif stayHit == "stay":
                    check = self.check("under_12")
                    
                    if check == "end":
                        break
                
                elif stayHit == False:
                    print()
                    self.end = input("Are you sure you want to quit? ").lower().strip()
                    print()
                    
                    if self.end == "yes":
                        return False
                    
                    elif self.end == "no":
                        continue
                    
                    else:
                        print("Invalid Input!")

        scores = self.stats.getScore()
        rounds = self.stats.getRoundsPlayed(self.numHand)
        percentage = self.stats.average()
        self.UI.endGame(scores, rounds, percentage)
        return False

    def check(self, checks):
        if checks == "empty":
            if self.deck.getMainDeck() == 0:
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
        
        if checks == "hit_one_card_remain":
            if self.deck.getMainDeck() <= 1:
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

                return "end"
       
        if checks == "under_12":
            if self.handSum < self.sumMin:
                self.UI.winLoseDisplay(None, "under_21", None)
                self.stats.increaseNumOfScore()
                self.handSum = 0
            else:
                self.stats.addScores(self.handSum)
                self.UI.winLoseDisplay("you_won", None, self.handSum)
                self.stats.increaseNumOfScore()
                self.handSum = 0
                return "end"

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

        

def runProgram():
    game = BlackJackGame()
    game.playGame()

if __name__ == "__main__":
    runProgram()

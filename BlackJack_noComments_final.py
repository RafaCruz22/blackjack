import random


class BlackJack:
    def __init__(self):
        self.deck = Deck()
        self.UI = UserInterface()
        self.stats = Statistics()
        self.sumCap = 21
        self.sumMin = 12
        self.handSum = 0
        self.numHand = 0

    def playGame(self):
        self.UI.gameIntro()
        deck = self.deck.getMainDeck()
        self.UI.displayCard("deck", None, deck)
        newGame = self.UI.playNewGame()
        if newGame == True:
            self.playRound()
        self.UI.endGame("beforeStart", 0, 0, 0)

    def playRound(self):
        print()
        while self.deck.getMainDeck() > 1:

            self.numHand += 1
            self.UI.headingPrint(self.numHand)

            for firstDeal in range(2):
                randSuit, cardValue = self.deck.dealCards()
                self.UI.displayCard("deal card", randSuit, cardValue)
                self.deck.decreaseMainDeck()
                self.handSum += cardValue
            self.UI.displayScore("curent score", self.handSum)
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
                    self.UI.displayScore("curent score", self.handSum)
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


class Deck:
    def __init__(self):
        self.mainDeck = 52
        self.suits = {
            "Spades": set(),
            "Clubs": set(),
            "Diamonds": set(),
            "Hearts": set(),
        }

    def getMainDeck(self):
        return self.mainDeck

    def resetAmount(self):
        self.mainDeck = 52

    def decreaseMainDeck(self):
        self.mainDeck -= 1

    def dealCards(self):
        suits = ["Spades", "Clubs", "Diamonds", "Hearts"]
        random.shuffle(suits)
        randomPick = random.randrange(0, len(suits))
        randSuit = suits[randomPick]
        if randSuit not in suits:
            randomPick = random.randrange(0, len(suits))
            randSuit = suits[randomPick]
        randomValue = random.randint(1, 13)
        while True:
            if randomValue not in self.suits[randSuit]:
                self.suits[randSuit].add(randomValue)
                return randSuit, randomValue
                break
            elif len(self.suits[randSuit]) != 13:
                for x in range(1, 20):
                    x = random.randint(1, 13)
                    if x not in self.suits[randSuit]:
                        randomValue = x
                        break
            elif len(self.suits[randSuit]) == 13:
                suits.remove(randSuit)
                randomPick = random.randrange(0, len(suits))
                randSuit = suits[randomPick]

    def resetDeck(self):
        self.suits = {
            "Spades": set(),
            "Clubs": set(),
            "Diamonds": set(),
            "Hearts": set(),
        }

    def getsuits(self):
        return self.suits


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
        avg = self.allScores / self.numOfScores
        return avg


class UserInterface:
    def gameIntro(self):
        print()
        gameInfo = (
            "\033[1m                                                           "
            + "\n                 - Welcome to BlackJack -                     "
            + "\n                                                              "
            + "\n     There are 52 card in a deck, 4 suits (Spades, Clubs,     "
            + "\n    Hearts, and Diamonds) each suit has 13 cards numbered     "
            + "\n    1 through 13. Every round you are dealt 2 cards. You      "
            + "\n   may request to be dealed another card 'hit' or you may     "
            + "\n   'stay'. If the sum of your hand is over 21 or under 12     "
            + "\n     you lose and get a score of zero for that round. If      "
            + "\n    you 'stay' between 12 and 21 you are given the sum of     "
            + "\n    your hand as your score. You keep playing rounds, until   "
            + "\n    the deck runs out of cards or you decided to quit the     "
            + "\n                       game at any time.                      "
            + "\n                                                              "
            + "\n                                                              "
            + "\n                         Good luck!                           "
            + "\n               May the odds be in your favor.                 "
            + "\n                                                      \033[0m "
        )
        print(gameInfo)
        print()

    def headingPrint(self, numHand):
        print()
        print(f" - Hand {numHand} - ")
        print()
        print("Cards")
        print("-" * 5)

    def deckDisplay(self, deckStatus):

        if deckStatus == "empty":
            print("Dealt hand over 21!")
            print("Bad Luck!")
            print("Points for hand : 0")

    def playNewGame(self):
        print()
        while True:
            user = input("Start BlackJack? (yes or no)").lower().strip()
            if user == "yes":
                return True
            elif user == "no":
                return False
            else:
                print("Invalid Input!")

    def stayHit(self):
        user = (
            input("Would you like to hit or stay? (Hit Enter To Quit Game) ")
            .lower()
            .strip()
        )
        if user == "":
            return False
        elif user == "hit":
            return "hit"
        elif user == "stay":
            return "stay"
        else:
            print("Invalid Input!")

    def displayScore(self, whichscore, score):

        if whichscore == "curent score":
            print()
            print(f"\033[1mScore : {score}\033[0m")
            print()

    def displayCard(self, whichCard, suit, value):
        if whichCard == "deal card":
            display = f"{suit}"
            display += f" {value}"
            print(display)

        elif whichCard == "deck":
            print(f"** Deck : {value} Cards **")
            print()

        elif whichCard == "hit card":
            print()
            print("Card")
            print("-" * 4)

    def winLoseDisplay(self, win, lose, score):

        if win == "you_won":
            print()
            print(f"You won {score} points!")

        if lose == "under_12":
            print("You lost, hand under 12.")
            print("Points for hand : 0")

        if lose == "dealt_lost":
            print("Dealt hand over 21!")
            print("Bad Luck!")
            print("Points for hand : 0")

        if lose == "over_21":
            print("You lost, went over 21!")
            print("Points for hand : 0")

    def endGame(self, end, score, hands, average):

        if end == "beforeStart":
            print()
            print("Thanks for Playing!")
            print()

        print()
        endGameMSG = (
            "                                                              "
            + f"\n    Scores                    |        {score}           ".rjust(10)
            + f"\n    Hands played              |        {hands}           ".rjust(10)
            + f"\n    Average Score             |        {average:.2f}     ".rjust(10)
            + "\n                                                          "
        )
        print(endGameMSG)
        print()


def main():
    Blackjack = BlackJack()
    Blackjack.playGame()


if __name__ == "__main__":
    main()

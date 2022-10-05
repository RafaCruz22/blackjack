from collections import defaultdict
from tkinter import E
from turtle import clear


class UserInterface:

    def __init__(self):
        self.cards = defaultdict(list)
        self.hiddenCard() 

    def gameIntro(self):

        gameInfo = (
            "  ********************************************************************************"
            + "\n  *                          - Welcome to BlackJack -                            *"
            + "\n  *                                                                              *"
            + "\n  *  There are 52 card in a deck, 4 suits (Spades, Clubs, Hearts, and Diamonds)  *"
            + "\n  *  each suit has 13 cards numbered 1 through 13. Every round you are dealt 2   *"
            + "\n  *  cards. You may request to be dealed another card 'hit' or you may 'stay'.   *"
            + "\n  *  If the sum of your hand is over 21 or under 12 you lose and get a score     *"
            + "\n  *  of zero for that round. If you 'stay' between 12 and 21 you are given the   *"
            + "\n  *  sum of your hand as your score. You keep playing rounds, until the deck     *"
            + "\n  *       runs out of cards or you decided to quit the game at any time.         *"
            + "\n  *                                                                              *"
            + "\n  *                                                                              *"
            + "\n  *                                Good luck!                                    *"
            + "\n  *                      May the odds be in your favor.                          *"
            + "\n  ********************************************************************************"
        )
        
        return gameInfo

    def banner(self, whichBanner : str, msg : str ):

        match whichBanner:
            case "complete": 
                print()
                print(("_" * 85) + "\n" )
                print(msg.center(60))
                print(("_" * 85) + "\n" )

            case "round": 
                print("_" * 85 )
                print(f" - Round {msg} - ".center(85))
                print(("_" * 85) + "\n" )
            
            case "top":
                print()
                print("_" * 85 )
                print()
                print(msg.center(60))

            case "bottom":
                print(msg.center(60))
                print("_" * 85 )
                print()

            case "deck":
                print(f"--> Deck: {msg} Cards <--\n")

            case "card":
                print()
                print("Cards")
                print("-" * 5)

            case _: 
                print("_" * 85 )

    def whosTurn(self,whom):
        msg = f"{whom} Hand"
        print(msg)
        print("-" * len(msg))

    def deckDisplay(self, deckStatus):

        if deckStatus == "empty":
            print("Dealt hand over 21!")
            print("Bad Luck!")
            print("Points for hand : 0")

    def playNewGame(self):
        print()
        while True:
            match input("Start BlackJack?: ").lower().strip():
                case "yes" | "y":
                    return True

                case "no" | "n":
                    return False

                case _:
                    print("\nInvalid Input!")

    def stayHit(self):
        while True:
            match input("Would you like to hit or stay? ").lower().strip():
                case "quit" | "q" | "":
                    return False

                case "hit" | "h":
                    return "hit"

                case "stay" | "s":
                    return "stay"

                case _:
                    print("\nInvalid Input!")

    def displayScore(self,score):
        print(f"Score : {score}")

    def displayWinner(self, whoWon, score):

        match whoWon:
            case "you_won":
                print()
                print(f"--> You won {score} points! <--".center(85))

            case "dealerWon":
                print("--> You lost, dealer has a better hand. <--".center(85))

            case "dealt_lost":
                print("--> Dealt hand over 21! <--".center(85))
                print("--> Bad Luck! <--".center(85))

            case "over_21":
                print("--> You lost, went over 21! <--".center(85))

    def gameStats(self, score, hands, average):
        custMSG = (
            "------------------------------------------------------\n".center(85)
            +"|                Thanks for Playing!                 |\n".center(56)
            +"------------------------------------------------------\n".center(84)
            +"| --> Money Won".rjust(10) + "|".rjust(15) + f"{score:>1} |\n".rjust(25)
            +"| --> Rounds".rjust(27) + "|".rjust(18) + f"{hands:>1} |\n".rjust(25)
            +"| --> Average Winning".rjust(36) + "|".rjust(9) + f"{average:>1} |\n".rjust(25)
            +"------------------------------------------------------".center(84)
        )

        print()
        print(custMSG)

    def quitGameDialog(self): 
        while True:
            match input("\t--> Are you sure you want to quit? ").lower().strip():
                case "yes" | "y":
                        return False
                    
                case "no" | "n":
                    break
                    
                case _:
                    print("Invalid Input!")

    def hiddenCard(self): 
        hiddenCard = [
            "|------------|",
            "|$$$$$$$$$$$$|",
            "|¢¢¢¢¢¢¢¢¢¢¢¢|",
            "|$$$$$$$$$$$$|",
            "|¢¢¢¢¢¢¢¢¢¢¢¢|",
            "|$$$$$$$$$$$$|",
            "|¢¢¢¢¢¢¢¢¢¢¢¢|",
            "|$$$$$$$$$$$$|",
            "|------------|"
        ]

        self.cards["hidden"] = hiddenCard

    def createCard(self,hand,hideCard):
        # print(hand)
        # ASCII conversion for card suits
        suits = {
            "hearts" : "\u2665", 
            "diamonds" : "\u2666",
            "clubs" : "\u2663",
            "spades" : "\u2660"
        }

        for card in hand: 
            rank = card[0]
            suit =  suits[card[1]]

            for line in range(0,9): 
                if line == 0: 
                    self.cards[line].append("|------------|")
                
                elif line == 1: 
                    self.cards[line].append(f"| {rank:<11}|")

                elif line == 4:
                    self.cards[line].append(f"|{suit:^12}|")

                elif line == 7:
                    self.cards[line].append(f"|{rank:>11} |")

                elif line == 8:
                    self.cards[line].append("|------------|")
                else: 
                    self.cards[line].append("|            |")

        self.displayCard(len(hand), hideCard)
        self.resetCards()

    def resetCards(self):
        self.cards = defaultdict(list)
        self.hiddenCard() 

    def displayCard(self,numCards, hideCard):
        if hideCard == "hide":
            for line in range(9):
                print(self.cards.get("hidden")[line], end = " ")
                for card in range(0,numCards-1):
                    print(self.cards[line][card], end= " ")
                
                print(" ")
                
        else: 
            
            for line in range(9): 
                for card in range(0,numCards):
                    print(self.cards[line][card], end= " ")
                
                print(" ")

if __name__ == "__main__":
    test = UserInterface()

    # test.gameStats(1,1,1)
    # test.gameStats(10,10,10)
    # test.gameStats(10000000,10000000,1000000)
    # test.gameStats(0,10,1000)

    test.createCard([[3, 'clubs'], [13, 'diamonds']],None)

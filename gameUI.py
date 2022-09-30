class UserInterface:
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
        print(gameInfo)
        print()

    def banner(self, whichBanner : str, msg : str ):

        if whichBanner == "complete": 
            print()
            print(("_" * 66 ).center(60))
            print()
            print(msg.center(60))
            print(("_" * 66 ).center(60))
            print()
        
        if whichBanner == "top":
            print()
            print(("_" * 66 ).center(60))
            print()
            print(msg.center(60))

        if whichBanner == "bottom":
            print(msg.center(60))
            print(("_" * 66 ).center(60))
            print()

        if whichBanner == "simpleLine": 
            print(("-" * 85 ).center(60))

    def headingPrint(self, numHand):
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
            input("Would you like to hit or stay? (Press 'Enter' To Quit) ")
            .lower()
            .strip()
        )
        if user == "":
            return False
        elif user == "hit" or user == "h":
            return "hit"
        elif user == "stay" or user == "s":
            return "stay"
        else:
            print("Invalid Input!")

    def displayScore(self,score):
        print()
        print(f"\033[1mScore : {score}\033[0m")
        print()

    def displayCard(self, whichCard, suit, value):
        if whichCard == "deal card":
            display = f"{suit} {value}"
            print(display)

        elif whichCard == "deck":
            print(f"** Deck: {value} Cards **")
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

    def gameStats(self, end, score, hands, average):

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

from collections import defaultdict


class UserInterface:
    ''' Handles all of the prints and displaying to the console. '''

    # --------------------------------------------------------------------------
    def __init__(self):
        '''Constuctor 
        post: cards'''
        self.cards = defaultdict(list)
        self.hiddenCard("ø")
        self.deckSymbol1 = "∫"
        self.deckSymbol2 = "∂"
        self.leftPadding = 13

    # --------------------------------------------------------------------------
    def hiddenCard(self, symbol):
        '''Hidden Card 
        post: adds the hidden card to the card list for displaying'''

        hiddenCard = [
            "|" + "|".rjust(13, "-"),  # 12
            "|" + "|".rjust(13, f"{symbol}"),
            "|" + "|".rjust(13, f"{symbol}"),
            "|" + "|".rjust(13, f"{symbol}"),
            "|" + "|".rjust(13, f"{symbol}"),
            "|" + "|".rjust(13, f"{symbol}"),
            "|" + "|".rjust(13, f"{symbol}"),
            "|" + "|".rjust(13, f"{symbol}"),
            "|" + "|".rjust(13, "-"),
        ]

        self.cards["hidden"] = hiddenCard

    # --------------------------------------------------------------------------
    def deckCard(self, deckCount):
        '''Deck Card prints the top of the deck 
        post: Deck with the number of cards in it'''

        deckCard = [
            "|" + "|".rjust(13, "-"),
            "|" + "|".rjust(13, f"{self.deckSymbol1}"),
            "|" + "|".rjust(13, f"{self.deckSymbol2}"),
            "|" + "|".rjust(13, f"{self.deckSymbol1}"),
            f"|---> {deckCount} <---|",
            "|" + "|".rjust(13, f"{self.deckSymbol1}"),
            "|" + "|".rjust(13, f"{self.deckSymbol2}"),
            "|" + "|".rjust(13, f"{self.deckSymbol1}"),
            "|" + "|".rjust(13, "-"),
        ]

        for line in deckCard:
            print(line)

        print()

    # --------------------------------------------------------------------------
    def gameIntro(self):
        '''Introduction to the game of blackjack 
        post: returns the messgae'''

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

    # --------------------------------------------------------------------------
    def banner(self, whichBanner: str, msg: str):
        '''Displays banners depending on which banner is needed
        post: prints the banner needed for the game'''

        match whichBanner:
            case "complete":
                print(("_" * 85) + "\n")
                print(msg.center(85))
                print(("_" * 85) + "\n")

            case "round":
                print("_" * 85)
                print(f" - Round {msg} - ".center(85))
                print(("_" * 85) + "\n")

            case "top":
                print()
                print("_" * 85)
                print()
                print(msg.center(60))

            case "bottom":
                print(msg.center(60))
                print("_" * 85)
                print()

            case "deck":
                print()
                print("Deck")
                print("-" * 4)

            case "card":
                print()
                print("Cards")
                print("-" * 5)

            case _:
                print("_" * 85)

    # --------------------------------------------------------------------------
    def whosTurn(self, whom):
        '''Prints who has the turn during the round
        post: prints if its the dealers or players turn'''

        msg = f"{whom} Hand"
        print(msg)
        print("-" * len(msg))

    # --------------------------------------------------------------------------
    def startDialog(self):
        '''Ask user if they want to play blackjack
        post: return True if user wants to play False otherwise'''

        print()
        while True:
            match input("\t--> Start BlackJack?: ").lower().strip():
                case "yes" | "y":
                    return True

                case "no" | "n":
                    return False

                case _:
                    print("--> Invalid Input!".rjust(self.leftPadding))
                    print(
                        "--> Type 'yes' or 'no' to start games.".rjust(self.leftPadding))

    # --------------------------------------------------------------------------
    def playerDecision(self):
        ''' Ask the use if they want to hit or stay
        post: return hit, stay if user chooses, False if they want to quit'''

        while True:
            match input("Would you like to hit or stay? ").lower().strip():
                case "quit" | "q" | "":
                    return False

                case "hit" | "h":
                    return "hit"

                case "stay" | "s":
                    return "stay"

                case _:
                    print("--> Invalid Input!")
                    print("--> Type 'hit' or 'stay'.")
                    print("--> Enter 'quit' or Press 'Enter' to quit game.")

    # --------------------------------------------------------------------------
    def quitDialog(self):
        '''Ask user if they want to quit game
        post: returns false if user doesn't want to quit, breaks if he does'''
        while True:
            match input("\t--> Are you sure you want to quit? ").lower().strip():
                case "yes" | "y":
                    return False

                case "no" | "n":
                    break

                case _:
                    print("--> Invalid Input!".rjust(self.leftPadding))
                    print(
                        "--> Type 'yes' or 'no' to quit game.".rjust(self.leftPadding))

    # --------------------------------------------------------------------------
    def displayScore(self, score):
        '''Displays the players current hand score
        post: prints the players score'''
        print(f"Score : {score}")

    # --------------------------------------------------------------------------
    def displayWinner(self, whoWon, score):
        '''Displays the winner of the round
        post: prints who won the hand/round'''

        match whoWon:
            case "you_won":
                print()
                print(f"--> You won {score} points!".rjust(self.leftPadding))

            case "dealerWon":
                print("--> You lost, dealer has a better hand.".rjust(self.leftPadding))

            case "dealt_lost":
                print("--> Dealt hand over 21!".rjust(self.leftPadding))
                print("--> Bad Luck! <--".rjust(self.leftPadding))

            case "over_21":
                print("--> You lost, went over 21!".rjust(self.leftPadding))

    # --------------------------------------------------------------------------
    def gameStats(self, wins, rounds, average):
        '''Displays the games stats
        pre: the amount of wins, rounds played and the average wins
        post: prints rounds won by plater, rounds played, and the average wins'''

        custMSG = (
            "------------------------------------------------------\n".center(
                85)
            + "|                Thanks for Playing!                 |\n".center(56)
            + "------------------------------------------------------\n".center(84)
            + "| --> Rounds Won".rjust(10) + "|".rjust(14) +
            f"{wins:>1} |\n".rjust(25)
            + "| --> Rounds Played".rjust(34) +
            "|".rjust(11) + f"{rounds:>1} |\n".rjust(25)
            + "| --> Average Winning".rjust(36) +
            "|".rjust(9) + f"{average:>1} |\n".rjust(25)
            + "------------------------------------------------------".center(84)
        )

        print()
        print(custMSG)

    # --------------------------------------------------------------------------
    def createCard(self, hand):
        '''Creates the cards that are displayed
        pre: the dealers or players cards
        post: adds the cards to a list for printing'''

        # ASCII conversion for card suits
        suits = {
            "hearts": "\u2665",
            "diamonds": "\u2666",
            "clubs": "\u2663",
            "spades": "\u2660"
        }

        for card in hand:
            rank = card[0]
            suit = suits[card[1]]

            for line in range(0, 9):
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

    # --------------------------------------------------------------------------
    def resetCards(self):
        ''' Resets the list of cards and appends the hidden card 
        post: a new list to contain cards with the hidden card'''
        self.cards = defaultdict(list)
        self.hiddenCard("ø")

    # --------------------------------------------------------------------------
    def displayCard(self, numCards, hideCard):
        '''Display Cards
        pre: the number of cards to display, "hide" if hidden card is required
        post: prints  the list of cards passed to it'''

        if hideCard == "hide":
            for line in range(9):
                print(self.cards.get("hidden")[line], end=" ")
                for card in range(0, numCards-1):
                    print(self.cards[line][card], end=" ")

                print(" ")

        else:
            for line in range(9):
                for card in range(0, numCards):
                    print(self.cards[line][card], end=" ")

                print(" ")


if __name__ == "__main__":
    ''' When file is ran. The test below will run. Futher proper testing is needed'''
    test = UserInterface()

    test.gameStats(1, 1, 1)
    test.gameStats(10, 10, 10)
    test.gameStats(10000000, 10000000, 1000000)
    test.gameStats(0, 10, 1000)

    test.createCard([[3, 'clubs'], [13, 'diamonds']])
    test.deckCard(52)

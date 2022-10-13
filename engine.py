from deckOfCards import Deck
from gameUI import UserInterface


class BlackJackEngine:
    ''' 
        Black Jack Engine. The engine contains all methods needed to run 
        a blackjack game. The engine also contains the statistics for the game.

        pre: requires deckofCard and gameUI modules 

    '''

    # --------------------------------------------------------------------------
    def __init__(self):
        '''Constructor 
        post: self is a game of blackjack '''
        self.deck = Deck()
        self.UI = UserInterface()
        self.stats = Statistics()
        self.sumMin, self.sumCap = 12, 21
        self.dealerScore, self.playerScore = 0, 0
        self.dealersHand, self.playersHand = [], []
        self.round = 0

    # --------------------------------------------------------------------------
    def start(self):
        ''' Starts Game
        post: prints the introduction message and banner, checks if user 
        wants to start a blckjack game, shuffles deck, prints statistic 
        when game ends 

        '''

        self.UI.banner("top", self.UI.gameIntro())

        newGame = self.UI.startDialog()
        if newGame == True:
            self.deck.shuffleDeck()
            self.playRound()

        self.showStats()

    # --------------------------------------------------------------------------
    def playRound(self):
        '''Starts A Round
        post: prints banner for the round, deals two cards to the player 
        and dealers to start a round. Reveals players hand and half of 
        the dealer'''

        while True:
            self.shuffle()

            # deals cards to player first then dealer. alternating cards dealt
            self.firstServe()

            deckCount = self.deck.getDeckCount()

            self.round += 1

            self.UI.banner("round", str(self.round))
            self.UI.banner("deck", None)
            self.UI.deckCard(deckCount)
            self.UI.banner("card", None)

            self.showHands("hideDealer")  # reveals hands

            # checks if player was dealt a hand over 21
            self.check("dealt_over_21")

            if self.playerChoice() == False:
                return False

    # --------------------------------------------------------------------------
    def shuffle(self):
        '''Shuffles self.deck

        Every three rounds the self.deck recreated and shuffled three times. 
        To simulate a real shuffle.  
        post: randomizes the order of cards in self'''

        if self.round % 3 == 0 and self.round >= 1:
            self.deck.resetDeck()
            for i in range(3):
                self.deck.shuffleDeck()
            self.UI.banner("complete", "--> Shuffle Successful <--")

    # --------------------------------------------------------------------------
    def firstServe(self):
        '''Deals four cards.
        The cards are dealt starting from the player then dealer twice
        post: initital card deal'''

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

    # --------------------------------------------------------------------------
    def playerChoice(self):
        '''Gives player option to hit or stay
        post: deals a card to player or deals cards to dealer. 
        returns false if player quits game'''

        while self.playerScore != 0:
            match self.UI.playerDecision():
                # player hit
                case "hit":
                    # might want to display CARD
                    suit, rank = self.deck.dealCard()
                    self.playersHand.append((rank, suit))
                    self.playerScore += rank
                    self.showHands("hideDealer")
                    self.check("over_21")

                # player Stayed
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

                # player wants to quit game
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

    # --------------------------------------------------------------------------
    def showHands(self, show):
        '''Reveals player and dealers hand depending if the round ends 
        or started
        pre: whoms hand to reveal. just the player or dealer and player
        post: prints the players or/and dealers hand 

        '''
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

    # --------------------------------------------------------------------------
    def viewDealer(self, hide):
        '''Reveals Dealers cards 
        pre: "hide" or None
        post: prints dealers hard, prints dealer banner
        '''
        self.UI.whosTurn("Dealer")
        self.UI.createCard(self.dealersHand)
        self.UI.displayCard(len(self.dealersHand), hide)
        self.UI.resetCards()

    # --------------------------------------------------------------------------
    def viewPlayer(self):
        '''Reveals Players cards 
        post: prints player hard, prints player banner
        '''
        self.UI.whosTurn("Player")
        self.UI.createCard(self.playersHand)
        self.UI.displayCard(len(self.playersHand), None)
        self.UI.displayScore(self.playerScore)
        self.UI.resetCards()
        print()

    # --------------------------------------------------------------------------
    def check(self, check):
        '''Evaluates hands
        pre: condition being checked for 
        post: winner of round. returns False if there is a winner'''
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
                    self.stats.increaseWin()
                    return False

            case "dealerWon":
                # not sure if equal who wins or nothing happens. temp: dealer must be strictly over player
                if (dealerWins | dealer21) and (dealerBust is False):
                    self.dealerWon()
                    return False

                elif dealerBust:
                    self.playerWon()
                    self.stats.increaseWin()
                    return False

            case _:
                print("No Match Found.")

    # --------------------------------------------------------------------------
    def playerWon(self):
        '''Player wins the round 
        post: prints both player and dealers hand. Alerts player that they won
        Increased round count and resets hands.
        '''
        self.showHands("both")
        self.UI.displayWinner("you_won", self.playerScore)
        self.stats.increaseRound()
        self.resetHands()

    # --------------------------------------------------------------------------
    def dealerWon(self):
        '''Dealer wins the round 
        post: prints both player and dealers hand. Alerts player that they lost
        Increased round count and resets hands.
        '''
        self.showHands("both")
        self.UI.displayWinner("dealerWon", None)
        self.stats.increaseRound()
        self.resetHands()

    # --------------------------------------------------------------------------
    def resetHands(self):
        ''' Resets both player and dealers hand and associated hand score 
        post: clears dealer and players hand and sets scores to zero '''
        self.dealersHand.clear()
        self.playersHand.clear()
        self.dealerScore, self.playerScore = 0

    # --------------------------------------------------------------------------
    def showStats(self):
        '''Displays game stats 
        post: players Score, number of rounds played, and winning percentage
        '''
        scores = self.stats.getWinnings()
        rounds = self.stats.getRoundsPlayed(self.round)
        percentage = self.stats.average()
        self.UI.gameStats(scores, rounds, percentage)


class Statistics:
    ''' 
        Keep track of the games rounds, score, and winning percentage
    '''
    # --------------------------------------------------------------------------

    def __init__(self):
        '''Constructor
        post: score,rounds and number of rounds set to zero'''

        self.timesWon = 0
        self.allRoundsPlayed = 0
        self.numOfRounds = 0

    # --------------------------------------------------------------------------
    def increaseWin(self):
        '''Games Score 
        post: increase player wins by 1'''
        self.timesWon += 1

    # --------------------------------------------------------------------------
    def getWinnings(self):
        '''Games Score 
        post: returns the total times the player has won'''
        return self.timesWon

    # --------------------------------------------------------------------------
    def increaseRound(self):
        '''Increase Rounds by 1
        post: number of rounds increments by 1'''
        self.numOfRounds += 1

    # --------------------------------------------------------------------------
    def getRoundsPlayed(self, rounds):
        '''Rounds played 
        post: returns the total amount of rounds played'''
        self.allRoundsPlayed += rounds
        return self.allRoundsPlayed

    # --------------------------------------------------------------------------
    def average(self):
        '''Average wining percentage
        post: returns the average times the player has won a hand'''
        try:
            avg = self.timesWon / self.numOfRounds
            return avg

        except:
            return 0


if __name__ == "__main__":
    test = BlackJackEngine()
    test.start()

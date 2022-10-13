import random


class Deck:
    '''Contains somethings needed to create a deck of cards'''

    # --------------------------------------------------------------------------
    def __init__(self):
        '''Constructor 
        post: creates a deck of cards in order 1-13. spades -> hearts'''

        self.deck = []
        self.suits = ["spades", "clubs", "diamonds", "hearts"]
        self.createDeck()

    # --------------------------------------------------------------------------
    def getDeckCount(self):
        '''Uses the built-in function to get length of list
        post: returns the current number of cards in the deck'''

        return len(self.deck)

    # --------------------------------------------------------------------------
    def createDeck(self):
        '''Creates the deck of cards
        pre: self.suits
        post: populates the deck list with cards, suit and rank'''

        for suit in self.suits:
            for rank in range(1, 14):
                self.deck.append((suit, rank))

    # --------------------------------------------------------------------------
    def dealCard(self):
        '''Deals a card to any player 
        post: removes the last index in the deck list'''

        return self.deck.pop(-1)

    # --------------------------------------------------------------------------
    def shuffleDeck(self):
        '''Shuffles the deck 
        post: randomizes the cards in the deck'''

        random.shuffle(self.deck)

    # --------------------------------------------------------------------------
    def resetDeck(self):
        '''Clears the deck of cards and recreates the deck
        post: a new deck of cards in order 1 - 13 spades -> hearts'''

        self.deck.clear()
        self.createDeck()


    # --------------------------------------------------------------------------
if __name__ == "__main__":
    '''When file is runned the below test is runed to check class methods 
    Needs more and proper testing'''

    test = Deck()

    # test.createDeck()

    for i in range(4):
        print(test.dealCard())

    for i in range(20):
        test.shuffleDeck()

    print("\nDeck Shuffle")

    for i in range(4):
        print(test.dealCard())

    test.resetDeck()
    print("\n", test.getDeckCount())

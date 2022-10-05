import random

class Deck:
    def __init__(self):
        self.deck = [] 
        self.suits = ["spades","clubs","diamonds","hearts"]
        self.createDeck()

    def getDeckCount(self):
        return len(self.deck)

    def createDeck(self):
        for suit in self.suits:
            for rank in range(1,14):
                self.deck.append((suit,rank))

    def dealCard(self): 
        return self.deck.pop(-1)

    def shuffleDeck(self):
        random.shuffle(self.deck)

    def resetDeck(self):
        self.deck.clear()
        self.createDeck()

if __name__ == "__main__":
    test = Deck()

    # test.createDeck()

    for i in range(4):
        print(test.dealCard())

    for i in range(20): 
        test.shuffleDeck()
    
    print("Deck Shuffle")
    
    for i in range(4):
        print(test.dealCard())

    test.resetDeck()
    print(len(test.getDeckCount))
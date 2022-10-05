import random

class Deck:
    def __init__(self):
        self.deckCount = 52
        self.suits = {
            "spades": set(),
            "clubs": set(),
            "diamonds": set(),
            "hearts": set(),
        }

    def getDeckCount(self):
        return self.deckCount

    def resetAmount(self):
        self.deckCount = 52

    def decreaseMainDeck(self):
        self.deckCount -= 1

    def dealCards(self):
        suits = ["spades", "clubs", "diamonds", "hearts"]
        random.shuffle(suits)
        randomPick = random.randrange(0, len(suits))
        randSuit = suits[randomPick]
        
        if randSuit not in suits:
            randomPick = random.randrange(0, len(suits))
            randSuit = suits[randomPick]
        #/ change randomValue to randomRank
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
            "spades": set(),
            "clubs": set(),
            "diamonds": set(),
            "hearts": set(),
        }

    def getsuits(self):
        return self.suits

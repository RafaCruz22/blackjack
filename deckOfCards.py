import random
import cards

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

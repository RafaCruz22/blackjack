
class Card: 

    def __init__(self):
        self.rank = [1,2,3,4,5,6,7,8,9,10,11,12,13] 
        self.suit = ["Spades", "Clubs", "Diamonds", "Hearts"]
        self.card = []
        
    def createCard(self):
        card = [self.rank[0],self.suits[0]]
        return self.card.append(card)

    

class PlayingCard: 

    def __init__(self):
        self.rank = [1,2,3,4,5,6,7,8,9,10,11,12,13] 
        self.suit = ["Spades", "Clubs", "Diamonds", "Hearts"]
        self.honourCard = {1 : "A", 11 : "J", 12 : "Q", 13 : "K"}
        self.card = []
        
    def createCard(self):
        self.card = [self.rank[0],self.suit[0]]
        return self.card
        
    def getCardRank(self): 
        return self.card[0]

    def getCardSuit(self):
        return self.card[1]
    

    
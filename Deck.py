
class Deck:

    def __init__(self,Cards):
        self.deck = []  # start with an empty list
        for x in self.suits:
            for y in self.ranks:
                self.deck.append(Card(suits,ranks))


    
    def __str__(self):
        return print(f'{self.deck}')

    def shuffle(self):
        random.shuffle(self.deck)
        
    def deal(self):
        pass
        
    


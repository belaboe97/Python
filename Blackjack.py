import random


suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,'Queen':10, 'King':10, 'Ace':11}

#GLOBAL VARIABLE
playing = True

class Card:
    
    def __init__(self,suits,ranks):
        self.suits = suits
        self.ranks = ranks
        
    
    def __str__(self):
        return print(f'Suits {self.suits} and Rank {self.ranks}')


class Deck:

    def __init__(self):
        self.deck = []  # start with an empty list
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit,rank))

    def __str__(self):
        deck_comp= ''
        for card in self.deck:
            deck_comp += card.ranks.__str__() + card.ranks.__str__()
        return deck_comp


    def shuffle(self):
        random.shuffle(self.deck)
        
    def deal(self):
        return self.deck.pop(0)



#test_deck = Deck()
#cards = Card('ace,','10')
#print(test_deck)
#print(type(cards.suits))
#test_deck.shuffle()
#print(test_deck)
#print(test_deck.deck[0].ranks,test_deck.deck[0].suits)
#print(len(test_deck.deck))
#test_deck.deal()

class Hand:
    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0
    
    def add_card(self,card):
        self.cards.append(card.ranks)
        for rank in values:
            if card.ranks == rank:
                self.value += values[rank]
        return self.value

    def adjust_for_ace(self):
        for ace in self.cards:
            if ace == 'Ace':
                while True: 
                    try:
                        tenOrOne = int(input('Please chose: Ace is value 11 or value 1'))
                        if tenOrOne is 1:
                            self.value -= 10
                            self.cards.pop(0)
                            break
                        elif tenOrOne is 11: 
                            break
                        else: 
                            continue
                    except:
                        print('You didnt entered a valid Number!')
                        continue

#newHand = Hand()
#newHand.add_card(Card('Hearts','Ace'))
#print(newHand.cards, newHand.value)
#newHand.adjust_for_ace()
#print(newHand.cards,newHand.value)

class Chips:
    
    def __init__(self,total=100,bet=10):
        self.total = total-bet
        self.bet = bet
        
    def win_bet(self):
        self.total += 2*self.bet
    
    def lose_bet(self):
        self.total -= self.bet


def take_bet():
    while True: 
        try:
            bet = int(input("Place you're bet"))
            return bet
        except:
            print('This was not a valid number')
            continue

#print(take_bet())

#def hit(deck,hand):
#    dealerHand = Hand()
 #   while True: 
  #      newCard = deck.deal() 
   #     hand.add_card(newCard)
    #    print(hand.value)
     #   choice = input('Do you want to pick anothger card? Y or N').upper()
      #  if choice == 'Y':
       #     if hand.value > 21:
        #        print("You have lost the game!")
         #   else: 
          #      continue
        #elif choice == 'N':
         #   dealerCard = deck.deal()
          #  hand.add_card(dealerCard)
           # dealerHand.add_card(dealerCard)
            #if dealerHand.value <= 17: 
             #   continue
            #else: 
               # break
#def hit(deck,hand):
 
#    while True: 
 #       newCard = deck.deal() 
  #      hand.add_card(newCard)
   #     choice = input('Do you want to pick anothger card? Y or N').upper()
    #    print(hand.value,hand.cards)
     #   if choice == 'Y': 
      #          if hand.value > 21: 
       #             hand.adjust_for_ace()
        #            if hand.value > 21:
         #               print(f'Hit {hand.value} You have lost!')
          #              break
                    
        #elif choice =='N':
         #   return hand.value  
       # else: 
        #    print('Pleaser hit Y or N')
         #   continue
   
def hit(deck,hand):
    newCard = deck.deal() 
    hand.add_card(newCard)
    if hand.value > 21: 
        print(f"You're actual score is: {hand.value}")
        hand.adjust_for_ace()
    return hand.value

#hit(test_deck,newHand)


def hit_or_stand(deck,hand):
    print(f'youre handscore is {hand.value}')
    value = hand.value
    global playing
    while True: 
        choice = input('Do you want to pick another card? Y or N').upper()
        if choice == 'Y':
            value += hit(deck,hand)
            print(value)
            continue
        if choice == 'N':
            playing = False
            break
    return value


#hit_or_stand(test_deck,newHand)

def show_some(playerHand,dealerHand):
    for card in playerHand.cards:
        print(f'Your Card is: {card}')

    print(f'The Dealerscard is:{dealerHand.cards[0]}')
  

def show_all(playerHand,dealerHand):
    for playercard in playerHand.cards:
        print(f'Your Card is: {playercard}')
    
    for dealercard in playerHand.cards:
        print(f'Your Card is: {dealercard}')

def player_busts(chips):
    chips.lose_bet()


#def player_wins(playerhand,dealerhand,deck,chips):
#    playerValue = hit_or_stand(deck, playerhand)
#    while True:
#        if hit(deck,dealerhand) < 17:
#            continue
#        elif hit(deck,dealerhand) > 21:
#            print('Player have won')
#            chips.win_bet()
#        elif hit(deck,dealerhand) < playerValue:
#            chips.win_bet()
#           break
def player_wins(deck,playerhand,dealerhand,chips):
    if hit(deck,playerhand) > hit(deck,dealerhand):
        chips.win_bet
        
def dealer_busts(deck,dealerhand,chips):
    if hit(deck,dealerhand) >= 17:
        if hit(deck,dealerhand) > 21:
            chips.win_bet()
            
    
def dealer_wins(deck,playerhand,dealerhand,chips):
    if hit(deck,dealerhand) > hit(deck,playerhand):
        chips.lose_bet()
       
def push(deck,playerhand,dealerhand):
    if hit(deck,playerhand) == hit(deck,dealerhand):
        print('Nobody has won')
    
while True:
    # Print an opening statement

    print('Welcheome to my First Ever Handmade Simplyfied BlackJack Game!')
    
    # Create & shuffle the deck, deal two cards to each player
    gameDeck = Deck()
    gameDeck.shuffle()
    playerHand = Hand()
    dealerHand = Hand()
    for x in range(0,2):
        playerValue = hit(gameDeck,playerHand)
        dealerValue = hit(gameDeck,dealerHand)

    # Set up the Player's chips
    chipStack = Chips()
    # Prompt the Player for their bet
    take_bet()

    # Show cards (but keep one dealer card hidden)
    show_some(playerHand,dealerHand)
    
    while playing:  # recall this variable from our hit_or_stand function

        # Prompt for Player to Hit or Stand
        playerHandValue = hit_or_stand(gameDeck,playerHand)
        if playerHandValue > 21:
            print('You Lost')
            player_busts(chipStack)
            show_some(playerHand,dealerHand)
            break
        # Show cards (but keep one dealer card hidden)
        show_some(playerHand,dealerHand)
        
        # If player's hand exceeds 21, run player_busts() and break out of loop

    # If Player hasn't busted, play Dealer's hand until Dealer reaches 17
        
        # Show all cards
        show_all(playerHand,dealerHand)
    
        # Run different winning scenarios
        player_wins(gameDeck,playerHand,dealerHand,chipStack)
        dealer_busts(gameDeck,dealerHand,chipStack)
        dealer_wins(gameDeck,playerHand,dealerHand,chipStack)
        dealer_wins(gameDeck,playerHand,dealerHand,chipStack)
        push(gameDeck,playerhand,dealerhand)
    # Inform Player of their chips total 
        print(chipStack.total)
    
    # Ask to play again
        
    break




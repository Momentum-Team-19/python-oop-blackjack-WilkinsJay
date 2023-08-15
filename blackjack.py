import random

SUITS = ['❤', '♦', '♠', '♣']
RANKS = ['A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K']


class Deck:
    def __init__(self, suits, ranks):
        self.cards = []
        for suit in suits:
            for rank in ranks:
                card = Card(suit, rank, value=0)
                if card.rank in ['J', 'Q', 'K']:
                    card.value = 10
                elif card.rank == 'A':
                    card.value = 11
                else:
                    card.value = card.rank
                self.cards.append(card)
    
    def shuffle(self):
        random.shuffle(self.cards)
    
    def draw_card(self):
        card = self.cards.pop()
        return card


class Card:
    def __init__(self, suit, rank, value):
        self.suit = suit
        self.rank = rank
        self.value = value

    def __str__(self):
        return f'{self.suit} {self.rank}'


class Player:
    def __init__(self):
        self.name = input('Please enter your name here:')
        self.hand = []
        self.score = 0


class Dealer:
    def __init__(self):
        self.name = 'Dealer Biggie'
        self.hand = []
        self.score = 0


new_deck = Deck(SUITS, RANKS)
new_deck.shuffle()


new_player = Player()


new_dealer = Dealer()


while len(new_player.hand) < 2:
    new_player.hand.append(new_deck.draw_card())
print(new_player.name)
for card in new_player.hand:
    new_player.score += card.value
    print(card)
print(new_player.score)

while len(new_dealer.hand) < 2:
    new_dealer.hand.append(new_deck.draw_card())
print(new_dealer.name)
for card in new_dealer.hand:
    new_dealer.score += card.value
    print(card)
print(new_dealer.score)





# user_card = Card(K, '❤')
# print(user_card)
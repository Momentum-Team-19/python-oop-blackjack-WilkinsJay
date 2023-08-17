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


class Game:
    def __init__(self):
        self.deck = Deck(SUITS, RANKS)
        self.deck.shuffle()
        self.player = Player()
        self.dealer = Dealer()

    def play_game(self):
        self.dealer.hand.append(self.deck.draw_card())
        while len(self.player.hand) < 2:
            self.player.hand.append(self.deck.draw_card())
        print(self.player.name)
        for card in self.player.hand:
            self.player.score += card.value
            print(card)
        print(self.player.score)

        while len(self.dealer.hand) < 2:
            self.dealer.hand.append(self.deck.draw_card())
        print(self.dealer.name)
        for card in self.dealer.hand:
            self.dealer.score += card.value
            print(card)
        print(self.dealer.score)
        if self.player.score == 21 or self.dealer.score == 21:
            if self.dealer.score < 21:
                print('Player has blackjack!')
                self.declare_winner()
                return
            elif self.player.score < 21:
                print('Dealer has blackjack 😕')
                self.declare_winner()
                return
            else:
                print()
        if self.player.score < 21:
            self.player_hit()
        if self.player.score <= 21:
            self.dealer_hit()
        self.declare_winner()

    def player_hit(self):
        action = None
        while action != 's':
            action = input('[h]it or [s]tay ').lower().strip()
            if action == 'h':
                self.player.hand.append(self.deck.draw_card())
                self.player.score = sum(
                    card.value for card in self.player.hand)
                if 'A' in [card.rank for card in self.player.hand] and self.player.score > 21:
                    self.player.score -= 10
                print('value:', self.player.score)
                for card in self.player.hand:
                    print(card)
                if self.player.score > 21:
                    print('Dang I just busted!')
                    break
                elif self.player.score == 21:
                    print('21 21!!')
                    break
            elif action != 's':
                print('Invalid choice. Enter h or s')
        else:
            print('You stayed, good choice 😏')

    def declare_winner(self):
        if self.player.score > 21:
            print('Dealer won that hand')
        elif self.dealer.score > 21:
            print('Player won that hand')
        elif self.player.score <= 21 and self.dealer.score <= 21:
            if self.player.score == self.dealer.score:
                print("It's a draw")
            elif self.player.score > self.dealer.score:
                print('Player won that hand')
            else:
                print('Dealer won that hand')

    def dealer_hit(self):
        print('Dealers turn:')
        while self.dealer.score < 17:
            self.dealer.hand.append(self.deck.draw_card())
            self.dealer.score = sum(
                card.value for card in self.dealer.hand)
            print('Dealer Biggie')
            for card in self.dealer.hand:
                print(card)
            print('dealers score:', self.dealer.score)
            if self.dealer.score > 21:
                print('HOORAYYY the dealer BUSTED!')
                break
            elif self.dealer.score == 21:
                print('Dealer got 21')
                break

new_game = Game()
new_game.play_game()

# user_card = Card(K, '❤')
# print(user_card)
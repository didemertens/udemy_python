import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
         'Queen':10, 'King':10, 'Ace':11}

playing = True

class Card:

  def __init__(self,suit,rank):
    self.suit = suit
    self.rank = rank

  def __str__(self):
    return f'{self.rank} of {self.suit}'


class Deck:

  def __init__(self):
    self.deck = []
    for suit in suits:
      for rank in ranks:
        self.deck.append(Card(suit,rank))

  def __str__(self):
    deck_string = ''
    for card in self.deck:
      deck_string += str(card) + '\n'
    return deck_string

  def shuffle(self):
    random.shuffle(self.deck)

  def deal(self):
    single_card = self.deck.pop()
    return single_card

#test_deck = Deck()
#print(test_deck)

class Hand:
  def __init__(self):
    self.cards = []
    self.value = 0
    self.aces = 0

  def add_card(self,card):
    self.cards.append(card)
    self.value += values[card.rank]
    if card.rank == 'Ace':
      self.aces += 1

  def adjust_for_ace(self):
    while self.value > 21 and self.aces:
      self.value -= 10
      self.aces -= 1

'''
test_deck = Deck()
test_deck.shuffle()
test_player = Hand()
test_player.add_card(test_deck.deal())
test_player.add_card(test_deck.deal())
print(test_player.value)

for card in test_player.cards:
  print(card)
'''

class Chips:

  def __init__(self):
    self.total = 100
    self.bet = 0

  def win_bet(self):
    self.total += self.bet

  def lose_bet(self):
    self.total -= self.bet


def take_bet(chips):
  while True:
    try:
      chips.bet = int(input('What is your bet? '))
    except ValueError:
      print('Please enter a valid number.')
      continue
    else:
      if chips.bet > chips.total:
        print('Your bet cannot be more than your total.')
        continue
      else:
        print('Bet placed.')
        break

def hit(deck,hand):
  hand.add_card(deck.deal())
  hand.adjust_for_ace()

def hit_or_stand(deck,hand):
  global playing
  while True:
    player_choice = input('Do you want to Hit or Stand?')
    if player_choice[0].lower() == 'h':
      hit(deck,hand)
    elif player_choice[0].lower() == 's':
      playing = False
    else:
      print('Sorry, try again.')
      continue
    break

def show_some(player,dealer):
  print("Dealer's Hand:")
  print('First card is hidden')
  print(dealer.cards[1])
  print("Player's Hand:", *player.cards, sep='\n')

def show_all(player,dealer):
  print("Dealer's Hand:", *dealer.cards, sep='\n')
  print("Total value Dealer:", str(dealer.value))
  print("Player's Hand:", *player.cards, sep='\n')
  print("Total value Player:", str(player.value))

def player_busts():
  print('Player busts.')
  chips.lose_bet()

def player_wins():
  print('Player wins.')
  chips.win_bet()

def dealer_busts(player,dealer,chips):
  print("Dealer busts!")
  chips.win_bet()

def dealer_wins(player,dealer,chips):
  print("Dealer wins!")
  chips.lose_bet()

def push(player,dealer):
  print('Dealer and Player tie. It is a push.')

while True:
  print('Welcome to BlackJack! Try to get as close to 21 as possible.')
  deck = Deck()
  deck.shuffle()
  # Deal 2 cards to each player

  player_hand = Hand()
  player_hand.add_card(deck.deal())
  player_hand.add_card(deck.deal())

  dealer_hand = Hand()
  dealer_hand.add_card(deck.deal())
  dealer_hand.add_card(deck.deal())

  # Set up the player's chips + take bet
  player_chips = Chips()
  take_bet(player_chips)

  # Show cards (but keep one dealer card hidden)

  show_some(player_hand, dealer_hand)

  while playing:
    hit_or_stand(deck, player_hand)
    show_some(player_hand, dealer_hand)

    if player_hand.value > 21:
      player_busts(player_hand,dealer_hand,player_chips)
      break

  if player_hand.value <= 21:
    while dealer_hand.value < 17:
      hit(deck,dealer_hand)

    show_all(player_hand, dealer_hand)

    if dealer_hand.value > 21:
      dealer_busts(player_hand,dealer_hand,player_chips)

    elif dealer_hand.value > player_hand.value:
      dealer_wins(player_hand,dealer_hand,player_chips)

    elif dealer_hand.value < player_hand.value:
      player_wins(player_hand,dealer_hand,player_chips)

    else:
      push(player_hand,dealer_hand)

  print("\nPlayer's winnings stands at",player_chips.total)
  new_game = input('Play again? Y/N')

  if new_game[0].lower() == 'y':
    playing = True
    continue
  else:
    print('Thanks for playing!')
    break

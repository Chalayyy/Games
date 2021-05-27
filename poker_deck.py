import random


class Card():
	# defines the cards used in the Deck class

	suits = ["Hearts", "Diamonds", "Spades", "Clubs"]
	values = ["A", "K", "Q", "J", "10", "9", "8", "7", "6", "5", "4", "3", "2"]

	# initialize each card
	def __init__(self, value, suit):
		self.value = value
		self.suit = suit

	# printing card tells value and suit
	def __repr__(self):
		return f"{self.value} of {self.suit}"

class Deck():
	# defines a deck that can be used for poker

	# initialize deck. It contains all 52 cards
	def __init__(self):
		self.cards = [Card(v,s) for v in Card.values for s in Card.suits ]
		
	# printing deck tells how many cards remain
	def __repr__(self):
		return f"Deck of {self.count()} cards"

	# count returns current size of deck (used in shuffle and _deal)
	def count(self):
		return len(self.cards)

	# _deal is a "private" function called in deal_card and deal_hand
	# if deck is empty, raise error. If not enough cards, deal remaining
	def _deal(self, num):
		count = self.count()
		actual = min([count,num])
		if count == 0:
			raise ValueError("All cards have been dealt")
		cards = self.cards[-actual:]
		self.cards = self.cards[:-actual]
		return cards

	# deals a single card (unnecessary? same as deal_hand(1))
	def deal_card(self):
		return self._deal(1)[0]

	# deals a number of cards 
	def deal_hand(self, hand_size):
		return self._deal(hand_size)
		
	# shuffles a full deck
	def shuffle(self):
		if self.count() == 52:
			return random.shuffle(self.cards)
		else:
			raise ValueError("Only full decks can be shuffled")
		

class Hand():
	# defines the hand of cards each player has

	# initialize hand by giving hand_size number of cards from deck to player
	def __init__(self, hand_size, deck, player):
		self.card_list = deck.deal_hand(hand_size)
		self.deck = deck
		self.player = player

	# printing hand 
	def __repr__(self):
		return f"{self.player}'s hand is {self.card_list}"

	# Exchange a chosen number of cards (consider using .remove or del)
	def exchange(self):
		ex_num = int(input("How many cards do you want to change? "))
		ex = []
		for i in range(0,ex_num):
			ex.append(int(input("Choose one card at a time to exchange: \n(e.g. type 2 to swap the second card)")))
		ex.sort(reverse=True)
		[self.card_list.pop(element-1) for element in ex]
		new = self.deck.deal_hand(ex_num)
		self.card_list.extend(new) 

	# def exchange(self):
	# 	exchange_amount = int(input("How many cards do you want to change? "))
	# 	# ex = [int(card) for card in input("Which cards do you want to exchange? ").split()]
	# 	lst1 = [int(item) for item in input("Enter the list items : ").split()] 
	# 	for item in lst1[::-1]:
	# 		self.card_list.pop(item-1)
	# 	self.card_list.append(self.deck.deal_hand(exchange_amount))


def calculate_hand(player):
	# determines what a player's final hand is to see who wins

	hand = "High Card"

	match = [card1.value == card2.value for card1 in player.card_list[:4] for card2 in player.card_list[player.card_list.index(card1)+1::]]
	count = match.count(True)
	# any matching values
	# 0 mactching = []
	# 1 pair = [True]
	# 2 pair = [True,True]
	# 3 oak = [True,True,True]
	# 4 oak = [True,True,True,True,True,True]
	# fh = [True,True,True,True]

	if count > 0:
		if count == 1:
			hand = "One Pair"
		elif count == 2:
			hand = "Two Pair"
		elif count == 3:
			hand = "Three of a kind"
		elif count == 4:
			hand = "Full House"
		elif hand == 6:
			hand = "Four of a kind"
		else:
			print("Hand Error")
			print(match)

	else:
		if any(
			(all([card.suit == "Hearts" for card in player.card_list]),
			all([card.suit == "Clubs" for card in player.card_list]),
			all([card.suit == "Spades" for card in player.card_list]),
			all([card.suit == "Diamonds" for card in player.card_list])
			)):
			hand = "Flush"

		if set(card.value for card in player.card_list) in straights:
			if hand == "Flush":
				if "A" in set(card.value for card in player.card_list):
					hand = "Royal Flush"
				else:
					hand = "Straight Flush"
			else:
				hand = "Straight"

	return hand

# all possible hands. Earlier hands beat later hands. Cannot distinguish ties yet
Winning_hands = [
	"Royal Flush", 
	"Straight Flush"
	"Four of a Kind", 
	"Full House", 
	"Flush", 
	"Straight", 
	"Three of a kind",
	"Two Pair",
	"One Pair",
	"High Card"
	]

straights = [set((Card.values+["A"])[s:s+5]) for s in range(0,10)]  # every possible set of straights


def play():
	# plays a two player game of poker

	# create and shuffle starting deck
	d = Deck()
	d.shuffle()

	# player1
	p1 = Hand(5, d, "Jen")
	print(str(p1))
	p1.exchange()
	print(str(p1))
	p1_hand = calculate_hand(p1)
	print(p1_hand)

	# player2
	p2 = Hand(5, d, "Charlie")
	print(str(p2))
	p2.exchange()
	print(str(p2))
	p2_hand = calculate_hand(p2)
	print(p2_hand)

	# see who wins
	if Winning_hands.index(p1_hand) < Winning_hands.index(p2_hand):
		print(f"{p1.player} wins!")
	elif Winning_hands.index(p1_hand) == Winning_hands.index(p2_hand):
		print("Draw!")
	else:
		print(f"{p2.player} wins!")


play()













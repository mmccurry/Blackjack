import random
import os

class Deck():

	def __init__(self):
		self.ordered_deck = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace",
		"2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace",
		"2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace",
		"2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]	

		self.card_value = {"2" : 2, "3" : 3, "4" : 4, "5" : 5, "6" : 6, "7" : 7, "8" : 8, "9" : 9, 
		"10" : 10, "Jack" : 10, "Queen" : 10, "King" : 10, "Ace" : 11}

		self.current_deck = []

	def reset_deck(self):
		self.current_deck = self.ordered_deck.copy()

	def shuffle(self):
		random.shuffle(self.current_deck)

	def draw_card(self):
		return self.current_deck.pop()

class Hand():
	def __init__(self, deck):
		self.hand = []
		self.hand_values = []
		self.aces = 0
		self.total = 0

	def deal(self):
		self.hand.append(deck.draw_card())
		self.hand_values.append(deck.card_value[self.hand[-1]])

		if self.hand[-1] == "Ace":
			self.aces += 1

		self.total += self.hand_values[-1]

		while self.total > 21 and self.aces > 0:
			self.total -= 10
			self.aces -= 1

	def reset_hand(self):
		self.hand = []
		self.hand_values = []
		self.aces = 0
		self.total = 0	

def game_start():
	os.system('clear')
	deck.reset_deck()
	deck.shuffle()
	player.reset_hand()
	dealer.reset_hand()
	player.deal()
	player.deal()
	dealer.deal()
	dealer.deal()
	
	for card in player.hand:
		if card == "Ace" or card == "8":
			print("You drew an " + card + ".")
		else:
			print("You drew a " + card + ".")
	print("Your total is " + str(player.total) + ".")

	if dealer.hand[0] == "Ace" or dealer.hand[0] == "8":
		print("\nThe dealer drew an " + dealer.hand[0] + ".")
	else: 
		print("\nThe dealer drew a " + dealer.hand[0] + ".")		

	hit_or_stand()
	
def hit_or_stand():
	print("Would you like to hit (h) or stand (s)?")
	choice = input("> ")

	if choice == "hit" or choice == "h":
		hit()
	elif choice == "stand" or choice == "s":
		dealer_choice()
	else:
		hit_or_stand()

def hit():
	player.deal()

	if player.hand[-1] == "Ace" or player.hand[-1] == "8":
		print("\nYou drew an " + player.hand[-1] + ".\nYour total is " + str(player.total) + ".")
	else:
		print("\nYou drew a " + player.hand[-1] + ".\nYour total is " + str(player.total) + ".")

	if player.total > 21:
		choose_winner()
	else:
		hit_or_stand()			

def dealer_choice():
	if dealer.total < 17:
		dealer.deal()
		dealer_choice()

	else:
		for card in dealer.hand[1:]:
			if card == "Ace" or card == "8":
				print("The dealer drew an " + card + ".")
			else:
				print("The dealer drew a " + card + ".")

		print("The dealer's total is " + str(dealer.total) + ".")			
		choose_winner()											

def choose_winner():
	if player.total > 21:
		print("You busted.\nThe dealer wins.")
	elif dealer.total > 21:
		print("The dealer busted.\nYou win.")
	elif dealer.total == player.total:
		print("It's a tie.")
	elif dealer.total > player.total:
		print("The dealer wins.")
	else:
		print("You win.")

	game_over()				

def game_over():
	print("Would you like to play again (p) or quit (q)?")
	choice = input("> ")

	if choice == "play again" or choice == "p":
		game_start()
	elif choice == "quit" or choice == "q":
		print("Thank you for playing.")
		exit(0)	

deck = Deck()
player = Hand(deck)
dealer = Hand(deck)

game_start()



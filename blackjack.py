import random
import os
import sys
import json

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
		self.money = 0
		self.bet = 0
		self.name = ""

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
		self.bet = 0

def clear_screen():
	if sys.platform == 'win32':
		os.system('cls')
	else:	
		os.system('clear')

def print_screen():
	clear_screen()

	print("""
----------------------------------------""")
	print("           Blackjack         Money: " + str(player.money)) 
	print("""----------------------------------------

  ---------              ---------
  |J      |              |A      |
  |   _   |              |   ^   |
  |  ( )  |              |  / \\  |
  | (_'_) |              |  \\ /  |
  |   |   |              |   v   |
  |      J|              |      A| 
  ---------              ---------         

----------------------------------------""")                  
	print("Your Cards: " + ", ".join(player.hand) ,)
	print(
"""----------------------------------------""")
	print("Your total: " + str(player.total))
	print(
"""----------------------------------------""")
	print("Dealer's cards: " + ", ".join(dealer.hand))  
	print(
"""----------------------------------------""")        
	print("Dealer's Total: " + str(dealer.total))
	print(
"""----------------------------------------""")		

def create_file():
	if os.path.isfile('blackjack_save.json') == False:
		save_games = open('blackjack_save.json', 'w')
		save_games.write('{}')
		save_games.close()	

def load_game():
	create_file()
	clear_screen()

	with open('blackjack_save.json', 'r') as save:
		save_games = json.load(save)

	print("To start a new game press (n).\nTo continue a previous game press (c).\nTo see a list of current saves press (s)")
	choice = input("> ")

	if choice == "n":
		while player.name == "":
			print("Please enter your name.")
			name = input("> ")

			if name.lower() in save_games:
				print("That name is already taken.")
			else:
				player.name = name.lower()
				player.money = 100	
				game_reset()

	elif choice == "c":
		while player.name == "":
			print("Please enter your name.")
			name = input("> ")
			
			if name.lower() in save_games:
				player.name = name.lower()
				player.money = save_games[name.lower()]
				game_reset()
			else:
				print("No save data exists for " + name)

	elif choice == "s":
		clear_screen()
		print_saves()
		print("\nPress enter to return to the last screen.")
		input()
		load_game()		
	


	else:
		load_game()

def game_reset():
	deck.reset_deck()
	deck.shuffle()
	player.reset_hand()
	dealer.reset_hand()
	print_screen()
	bet()
	

def bet():
	print("How much do you want to bet?\nThe minimum bet is 5.")
	choice = input("> ")

	if choice.isdigit():
		if player.money - int(choice) < 0:
			print("You don't have enough money")
			bet()
		elif int(choice) < 5:
			print("The minimum bet is 5.")
			bet()
		else:		
			player.money -= int(choice)
			player.bet = int(choice)
			deal()
	else:
		print("You have to enter a number.")
		bet()
	
def deal():
	player.deal()
	player.deal()
	dealer.deal()
	hit_or_stand()

def hit_or_stand():
	print_screen()
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

	if player.total > 21:
		choose_winner()
	else:
		hit_or_stand()			

def dealer_choice():
	dealer.deal()

	while dealer.total < 17:
		dealer.deal()
				
	choose_winner()

def choose_winner():
	print_screen()
	if player.total > 21:
		print("You busted.\nThe dealer wins.")
	elif dealer.total > 21:
		player.money += player.bet * 2
		print_screen()
		print("The dealer busted.\nYou win.")
	elif dealer.total == player.total:
		player.money += player.bet
		print_screen()
		print("It's a tie.")
	elif dealer.total > player.total:
		print("The dealer wins.")
	else:
		player.money += player.bet * 2
		print_screen()
		print("You win.")

	if player.money < 5:
		low_money()
	else:
		game_over()

def low_money():
	print("Sorry, you don't have enough money to continue.\nWould you like to start a new game (n) or quit (q)")
	choice = input("> ")
	if choice == "n" or choice == "new game":
		delete_save()
		player.name = ""
		load_game()
	elif choice == "q" or choice == "quit":
		delete_save()
		clear_screen()
		sys.exit()
	else:
		print("I don't understand.")
		low_money()									

def game_over():
	choice = input("Would you like to play again (p) or quit (q)?\n> ")
	if choice == "play again" or choice == "p":
		game_reset()
	elif choice == "quit" or choice == "q":
		save_game()
		clear_screen()
		sys.exit()
	else:
		print("I don't understand.")
		game_over()	

def save_game():
	with open('blackjack_save.json', 'r') as save:
		save_games = json.load(save)
		save_games.update({player.name: player.money})
		
	with open('blackjack_save.json', 'w') as save:	
		json.dump(save_games, save)	
		
def delete_save():
	with open('blackjack_save.json', 'r') as save:
		save_games = json.load(save)

		if player.name in save_games:
			del save_games[player.name]

	with open('blackjack_save.json', 'w') as save:		
		json.dump(save_games, save)		

def print_saves():
	with open('blackjack_save.json', 'r') as save:
		save_games = json.load(save)
		for save in save_games:
			print(save + ": " + str(save_games[save]))

	print("\nPress enter to return to the last screen.")
	input()
	load_game()			


deck = Deck()
player = Hand(deck)
dealer = Hand(deck)

load_game()


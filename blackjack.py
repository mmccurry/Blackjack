import random

# Lists every card in a deck. Ignores suit because they aren't relevant to blackjack.
deck = ["2", "3", "4", "5", "6", "7","8", "9", "10", "Jack", "Queen", "King", "Ace",
"2", "3", "4", "5", "6", "7","8", "9", "10", "Jack", "Queen", "King", "Ace", "2", 
"3", "4", "5", "6", "7","8", "9", "10", "Jack", "Queen", "King", "Ace", "2", "3", "4",
"5", "6", "7","8", "9", "10", "Jack", "Queen", "King", "Ace"]

#Matches each card with its numerical value in blackjack
card_value = {"2" : 2, "3" : 3, "4" : 4, "5" : 5, "6" : 6, "7" : 7, "8" : 8, "9" : 9, "10" : 10, "Jack" : 10, "Queen" : 10, "King" : 10, "Ace" : 11}

#shuffles the deck, deals two cards and tells the user their cards
#and the total.
def deal():
	random.shuffle(deck)

	card_1 = deck.pop()
	card_2 = deck.pop()
	global total
	total = card_value[card_1] + card_value[card_2]
		
	print(f"Your cards are {card_1} and {card_2}")
	print(f"Your total is {total}")
	dealer_draw()

def dealer_draw():
	global dealer_card_1
	global dealer_card_2
	global dealer_total
	dealer_card_1 = deck.pop()
	dealer_card_2 = deck.pop()
	dealer_total = card_value[dealer_card_1] + card_value[dealer_card_2]

	print(f"The dealer has {dealer_card_1}")
	hit_or_stand()	

#lets user either hit, and receive another card, or stand
def hit_or_stand():
	print("Would you like to hit or stand?")
	choice = input("> ")

	if choice == "hit":
		card_3 = deck.pop()
		global total
		total = total + card_value[card_3]
		print(f"Your new card is {card_3}")
		if total > 21:
			print(f"Your total is {total}.\nYou busted")
		else:
			print(f"Your total is {total}")
			hit_or_stand()
	elif choice == "stand":
		dealer_cards()			
	else:
		print("You have to type hit or stand.")
		hit_or_stand()			

#prints the dealers cards
def dealer_cards():
	global dealer_card_1
	global dealer_card_2

	print(f"The dealer's cards are {dealer_card_1} and {dealer_card_2}")
	dealer_choice()

#The dealer draws cards until he has at least 17
def dealer_choice():
	global dealer_total
	
	if dealer_total < 17:
		dealer_card_3 = deck.pop()
		print(f"The dealer drew {dealer_card_3}")
		dealer_total = dealer_total + card_value[dealer_card_3]
		dealer_choice()
	else:
		winner()

#determines who the winner is
def winner():
	global dealer_total
	global total

	if dealer_total > 21:
		print(f"The dealer's total is {dealer_total}\nThe dealer busted.\nYou win!")
	elif dealer_total > total:
		print(f"The dealer's total is {dealer_total}\nYour total is {total}\nThe dealer wins.")
	else:
		print(f"The dealer's total is {dealer_total}\nYour total is {total}\nYou win!")				

deal()
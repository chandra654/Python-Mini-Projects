#Project 4 - Rock and Scissors Game

# Rules: There are 3 things called rock , scissor and paper.
# Winning Combinations : Rock > Sicissor and Scissor > Paper and Paper > Rock

import random
import time 

def play():

	possible_things = ['r' , 's' ,'p']

	print("\n\nWelcome to Rock and Scissors game!\n")
	print("\nChoose any one of these: R or r - Rock , S or s - Scissors and P or p - Paper")
	print("Type 'e or E' for exit !\n")

	while True:

		user_input = input("\nYou:").lower()

		if user_input == 'e':
			print("\nThnaks for playing !!\n")
			break

		computer_input = random.choice(possible_things)

		print(f"System:{computer_input}")

		time.sleep(0.35)

		print(game_status(user_input , computer_input),end="\n")
		
		time.sleep(0.7)

def game_status(user , computer):

	if user == computer:
		return "Tie"

	elif (user=='r' and computer=='s') or (user=='s' and computer=='p') or (user=='p' and computer=='r'):
		return 'You Won!!'
	else:
		return "System Won!!"



play()
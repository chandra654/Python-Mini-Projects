#Project No -  5 : Hangman game

import random
from data import data
from more_itertools import locate

def hangman():

	#generate a random word
	guessed_word = random.choice(data)

	#user_word - it is the word guessed by user upto now
	user_word = ["_" for i in range(len(guessed_word))]

	#avoid spaces and hypens
	while " " in guessed_word or "-" in guessed_word:
		guessed_word = random.choice(data)

	
	#playing the game
	lenght = len(guessed_word)
	used_letters = [] #it is used to track the letters already used by the user
	lives = 6

	print("\n\nWelcome to Hangman game !!")
	print("Fill these gaps to form a meaningful word:",end=" ")
	print(' '.join(user_word))

	while ''.join(user_word) != guessed_word and lives > 0:

		print(f"\n\nYou have {lives} lives left and used letters are: {' , '.join(used_letters)}")
		
		user_input = input("Type something:") #here user enters a letter
		
		while user_input in used_letters:
			print("\nYou already used that letter.")
			user_input = input('Type something:')
		
		used_letters.append(user_input)
	
		if user_input in guessed_word:
			
			#this is to find out the multiple indexes of a letter in the word using more_itertools package
			array_indexes = list(locate(list(guessed_word), lambda x: x == user_input))
			for arr in array_indexes:
				user_word[arr] = user_input

		else:
			lives = lives - 1


		print(' '.join(user_word))
	
	if lives <= 0:
		print(f"\nYou died ! You lost the game.correct word is {guessed_word}")
	else:
		print(f"\nYou won !! {user_word} is correct!")


hangman()
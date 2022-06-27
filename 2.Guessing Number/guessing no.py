#Project 2 - Guessing Number By User

import random

def guess(r):
	random_number = random.randint(1,r)

	guess_number = -1

	count = 0

	while guess_number != random_number:

		guess_number = int(input("\nGuess a number?:"))

		if guess_number < random_number:
			print("Sorry wrong answer!.Number is too low!!")

		if guess_number > random_number:
			print("Sorry wrong answer!.Number is too high!!")

		count = count + 1

	print(f"Correct answer ! You have guessed {random_number} correctly in {count} steps !!.")

print("\n\nWelcome to Guessing Number!!")
guess(int(input("\nBefore we begin game enter the range in which whithin you want to play:")))
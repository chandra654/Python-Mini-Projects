#Project 3 - Guessing number by system

#Using random.randint()

import random

def guess_by_system(r):
	low = 1 
	high = r

	feedback_from_user = ''

	count = 0

	while feedback_from_user.casefold() != 'c':

		#make a guess by system
		guess_by_system = random.randint(low , high)

		print(f"\nOur guess is {guess_by_system} is it too high (H or h) is it too low (L or l) or correct (C or c)",end=" ")
		feedback_from_user = input()

		if feedback_from_user.casefold() =='h':
			high = guess_by_system - 1

		if feedback_from_user.casefold() =='l':
			low = guess_by_system + 1

		count = count + 1

	print(f"\nSystem predicted {guess_by_system} correctly and  Game won by System in {count} steps")

print("\n\nWelcome to Guessing Number!!")
print("\n\nBefore we begin game guess a number and don't tell us")

guess_by_system(int(input("\nEnter range:")))
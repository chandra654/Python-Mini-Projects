#project No 1 - madlib game

def madlib():

	print("\nFill the blanks to form a exciting story:\n\n")

	print("\tEvery ____(month)___ we always have a picnic at ___(place)___. \n \
	We invite ___(friend1)___ and ___(friend2)___ .It is next to a very ____(adjective)____ lake.\n\
	There are __(animal1)__ and __(animal2)__ which are very ____(adjective2)___. \n\
	We eat lots of food that everyone ___(adjective3)____.\n\
	The games are my favorite part. \n\
	We play ___(game1)___ and ___(game2)___ until we can’t walk anymore.\n\
	Then we ___(verb)___ back and relax under the old shade tree until ___(noun)___ says,\n\
	'we need to go home !'")

	print("\nPlease fill the missing places in order:\n\n")
	month = input("Enter month name:")
	place = input("Enter place name:")
	friend1 = input("Enter friend name(friend1):")
	friend2 = input("Enter friend name(friend2):")
	adjective1 = input("Enter adjective1:")
	animal1 = input("Enter a animal name (animal1):")
	animal2 = input("Enter a animal name (animal2):")
	adjective2 = input("Enter adjective2:")
	adjective3 = input("Enter adjective3:")
	game1 = input("Enter game1:")
	game2 = input("Enter game1:")
	verb = input("Enter verb:")
	noun = input("Enter a noun:")

	print("\nThe final story is:\n\n")
	print(f"\tEvery {month} we always have a picnic at {place}.\n\
	We invite {friend1} and {friend2} .It is next to a very {adjective1} lake.\n\
	There are {animal1} and {animal2} which are very {adjective2}.\n\
	We eat lots of food that everyone {adjective3}.The games are my favorite part.\n\
	We play {game1} and {game2} until we can’t walk anymore.\n\
	Then we {verb} back and relax under the old shade tree until {noun} says,\n\
	'we need to go home !'")

madlib()
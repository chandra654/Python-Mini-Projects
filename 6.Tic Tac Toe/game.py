#Tic Tac Toe Game

import random
import time

#human player class
class HumanPlayer:

	def __init__(self , letter):
		self.letter = letter

	#selecting a spot to make a move	
	def pick_a_spot(self , game):

		valid_move = False

		while valid_move == False:
			
			move = int(input(f"Your Turn ? Enter a valid spot to place '{self.letter}':"))
			
			if move in game.available_moves():
				
				valid_move = True
				return move
			
			else:
				print("Invalid move!Please Try again!!")


#computer player class
class ComputerPlayer:

	def __init__(self , letter):
		
		self.letter = letter
 	
 	#selecting a spot to make a move
	def pick_a_spot(self , game):
		
		move = random.choice(game.available_moves())
		return move

#Game class
class TicTacToe:

	def __init__(self):
		self.board = [" " for i in range(9)]  #board as list representation
		
		self.winner = None
		

	#for printing the board values in a neat shape looks like a 3 x 3 grid	
	def print_board(self):
		
		print("\n")
		for i in range(3):
			print("  ",end=" ")
			for j in self.board[i*3:(i+1)*3]:
				print(f"| {j} " , end=" ")
			print("|")

			print("\n",end="\n")

	#for printing the indexes in the table format 3 x 3 grid layout		
	def print_board_numbers(self):
		
		print("\n")
		for i in range(3):
			print("  ",end=" ")
			for j in range(i*3 ,(i+1)*3):
				print(f"| {j} " , end=" ")
			print("|")

			print("\n",end="\n")



	def available_moves(self):
		return [i for i in range(9) if self.board[i] == " "]

	#for checking how many empty slots are present			
	def empty_slots(self):
		return len(self.available_moves())



	#here board is updated according to player's selected spot	
	def make_move_on_board(self , letter , spot):
		
		#spot = player.pick_a_spot(game)

		self.board[spot] = letter
		#self.available_moves.remove(spot)

		if letter == 'X':
			#time.sleep(0.5)
			print(f"\nSystem:'X' placed at {spot}")
			#time.sleep(0.3)

		else:
			print(f"\nYou:'o' placed at {spot}")
			#time.sleep(0.3)

		self.print_board()

		self.check_winner(letter , spot) #after every updation check for if there is a winner

	
	def check_winner(self , letter , spot):

		#row check winner
		row = spot//3

		if all([i == letter for i in self.board[row*3:(row+1)*3] ]):
			#print('Winning case')
			self.winner = letter
			return

		#colum check winner
		column = spot%3
		if all([i == letter for i in self.board[column:column+7:3]]):
			#print('Winning case')
			self.winner = letter
			return

		#diagonals winner

		#diagonal 1 - [ 0 , 4 , 8  ]
		if all([self.board[i] == letter for i in [0,4,8]]):
			#print('Winning case')
			self.winner = letter
			return

		#diagonal2 - [ 2 , 4 , 6]	
		if all([self.board[i] == letter for i in [2,4,6]]):
			#print('Winning case')
			self.winner = letter
			return




def play_game(game ,player1 , player2):


	nextplayer= None

	if player1.letter == 'X':
		
		spot = player1.pick_a_spot(game)

		game.make_move_on_board(player1.letter , spot)

		nextplayer=player2
	else:
		
		spot = player2.pick_a_spot(game)

		game.make_move_on_board(player2.letter , spot)
		
		nextplayer = player1

	while not game.winner and game.empty_slots():
		
		spot = nextplayer.pick_a_spot(game)
		
		game.make_move_on_board(nextplayer.letter , spot)

		nextplayer = player2 if nextplayer==player1 else player1



	if game.winner==None:
		
		print('\nIt\'s a Tie')
	
	else:
		
		if game.winner ==  'o':
			print('\nYou won the game ! The winner is \' ' , game.winner,'\'' )
		
		else:
			print('\nSorry!You lost the game , the game is won by the system!!.')





print("\n\nWelcome to Tic-Tac-Toe Game!!")
print("\nHello I am your opponent and my name is system.I choosed 'X' so you are playing with 'o'!!")

game = TicTacToe()

#time.sleep(0.5)

print("\nThis is a board , take a look:")
game.print_board_numbers()

#time.sleep(0.4)

print("Let's Play:")


human = HumanPlayer('o')
computer = ComputerPlayer('X')

play_game(game,human , computer)
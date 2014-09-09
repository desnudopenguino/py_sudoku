#This is a pythin sudoku board generator
import random
#create the board
def new_board(segment_size):
	row_size = column_size = segment_size ** 2 # set length and width of board
	#board array
	board = []
	# reset excludes and column count for each row
	for row_index in range(row_size):
		board.append([])
		for column_count in range(column_size):
			new_number = generate_number(row_size)
			board[row_index].append(new_number)
	return board

def generate_number(row_size):
	return random.randint(1,row_size)
			
def print_board(board):
	print "\n"
	print "Sudoku Board!"
	for row in board:
		print row

print_board(new_board(3))

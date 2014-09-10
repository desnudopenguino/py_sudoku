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
		used = []
		for column_count in range(column_size):
			new_number = generate_number(row_size, used)
			used.append(new_number)
			board[row_index].append(new_number)
	return board

#makes sure that unique numbers are in both rows and cols
def check_columns(board):
	for row in range(len(board)):
		for temp_row in range(len(board)):
			if temp_row != row:
				for col_index in range(9):
					if board[row][col_index] == board[temp_row][col_index]:
						board[temp_row].append(board[temp_row].pop(col_index))
		

def generate_number(row_size, used):
	new_number = random.randint(1,row_size)
	while new_number in used:
		new_number = random.randint(1,row_size)
			
	return new_number
def print_board(board):
	print "\n"
	print "Sudoku Board!"
	for row in board:
		print row

def generate_segment(row_size,used):
	segment = []
	count = 0
	while count < row_size ** .5:
		new_number = random.randint(1,row_size)
		while new_number in used:
			new_number = random.randint(1,row_size)
		segment.append(new_number)
		count += 1
	return segment 

def generate_block(row_size):
	block = []
	used = []
	for count in range(int(row_size ** .5)):
		new_segment = generate_segment(row_size,block)
		block.append(new_segment)
		used += new_segment
		print used
		print block

	return block

print generate_block(9)

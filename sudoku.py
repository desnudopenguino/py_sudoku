#This is a pythin sudoku board generator
import random
def generate_row():
	row = []
	counter = 0
	while counter < 9:
		new_number = random.randint(1,9)
		if new_number not in row:
			row.append(new_number)
			counter += 1
	return row

def generate_columns():
	columns = []
	counter = 0
	while counter < 9:
		new_row = generate_row()
		unique = True
		for index in columns:
			if check_rows(index,new_row) == False:
				unique = False
		if unique:
			columns.append(new_row)
			counter += 1
			print "Column found!"
	return columns

def check_rows(row1,row2):
	unique = True
	for index in range(len(row1)):
		if row1[index] == row2[index]:
			unique = False
	return unique

def print_board(board):
	for row in board:
		print row

#generate a 3-item list segment.  these are the building blocks for the sudoku board
def generate_segment(exclude):
	segment = []
	counter = 0
	while counter < 3:
		new_number = random.randint(1,9)
		if new_number not in segment and new_number not in exclude:
			segment.append(new_number)
			counter += 1
	return segment

# builds the 3x3 grid for one of the 9 "blocks" of the board
def generate_block(exclude):
	block = []
	counter = 0
	while counter < 3:
		new_segment = generate_segment(exclude)
		block.append(new_segment)
		exclude += new_segment
		counter += 1
	return block

def generate_block_row():
	row = []
	for index in range(3):

		new_block = generate_block()

		row.append()
	return row

def print_block(block):
	for segment in block:
		print segment

def print_block_row(row):
	for index in range(3):
		for block in row:
			print block[index] ,
		print "\n"

#create the board
def new_board(segment_size):
	row_size = segment_size ** 2
	#board array
	board = []
	# reset excludes and column count for each row
	for row_index in range(row_size):
		board.append([])
		for column_count in range(row_size):
			excludes = board[row_index]
			print len(board[row_index])
			new_number = new_generate_number(excludes,row_size)
			board[row_index].append(new_number)

	return board

def new_generate_number(excludes,row_size):
	new_number = random.randint(1,row_size)
	while new_number in(excludes):
		new_number = random.randint(1,row_size)
	return new_number
			
def new_print_board(board):
	for row in board:
		print row

new_print_board(new_board(3))

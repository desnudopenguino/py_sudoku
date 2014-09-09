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

def generate_block():
	block = []
	exclude = []
	counter = 0
	while counter < 3:
		new_segment = generate_segment(exclude)
		block.append(new_segment)
		exclude += new_segment
		counter += 1
	return block

def print_block(block):
	for segment in block:
		print segment

print_block(generate_block())

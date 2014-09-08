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

print_board(generate_columns())



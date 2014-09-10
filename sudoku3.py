
# this will generate a sudoku board
import random
def generate_board(size):
	full_size = size ** 2
	board = []
	used_positions = [] # [x,y] coords for used positions

	#initialize board
	for count in range(full_size):
		board.append([])
		for count2 in range(full_size):
			board[count].append(0)
	
	#generate grid position
	while check_board_full(used_positions) == False:
		x = random.randint(0,full_size-1)
		y = random.randint(0,full_size-1)
		position = [x,y]
		if check_used_position(position, used_positions) == False:
			#use other logic here to check if number is unique in row, col, & block
			number = random.randint(1,full_size)
			if check_row(number,x) and check_column(number,y) and check_block(number,x,y):
				board[x][y] = number
				used_positions.append([x,y])


	return board

def check_board_full(used_positions):
	if len(used_positions) < 81:
		return False
	else:
		return True

def check_used_position(position, used_positions):
	if position in used_positions:
		return True
	else:
		return False

def check_row(number, row_index):
	return True

def check_column(number, column_index):
	return True

def check_block(number, row_index, column_index):
	return True


def print_board(board):
	for row in board:
		for item in row:
			print item ,
		print "\b"

board = generate_board(3)
print_board(board)

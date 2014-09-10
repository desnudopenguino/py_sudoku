
# this will generate a sudoku board
import random
def generate_board(size):
	full_size = size ** 2
	board = []
	used_positions = [] # [x,y] coords for used positions
	iterations = 0

	#initialize board
	for count in range(full_size):
		board.append([])
		for count2 in range(full_size):
			board[count].append(0)
	
	#generate grid position
	invalid_counter = 0
	while check_board_full(used_positions) == False:
		iterations += 1
		pos = generate_position(full_size-1)
		if check_used_position(pos, used_positions) == False:
			#use other logic here to check if number is unique in row, col, & block
			number = random.randint(1,full_size)
			if check_row(number,pos[0],board) and check_column(number,pos[1],board) and check_block(number,pos[0],pos[1],board):
				board[pos[0]][pos[1]] = number
				used_positions.append(pos)
			else:
				invalid_counter += 1
			
			if invalid_counter == 50:
				reset_positions(pos[0],pos[1],board,used_positions)
				invalid_counter = 0
				#reset nome numbers

	print iterations
	return board

def generate_position(end):
	x = random.randint(0,end)
	y = random.randint(0,end)
	return [x,y]


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

def check_row(number, row_index, board):
	row = []
	for count in range(len(board)):
		row.append(board[row_index][count])
	if number in row:
		return False
	else:
		return True

def check_column(number, column_index, board):
	column = []
	for count in range(len(board)):
		column.append(board[count][column_index])
	if number in column:
		return False
	else:
		return True

def check_block(number, row_index, column_index, board):
	return True

# if the system becomes locked up, reset some numbers to 0 to see if it can correct itself.
def reset_positions(x_pos,y_pos,board,used_positions):
	length = len(board)-1
	x = random.randint(0,length)
	y = random.randint(0,length)
	while x == x_pos and y == y_pos:
		x = random.randint(0,length)
		y = random.randint(0,length)
	
	x_base = [x_pos,y]
	y_base = [x,y_pos]

	board[x_pos][y] = 0
	board[x][y_pos] = 0

	if x_base in used_positions:
		used_positions.remove(x_base)
	if y_base in used_positions:
		used_positions.remove(y_base)


def print_board(board):
	print "Sudoku Solved!" 
	for row in board:
		for item in row:
			print item ,
		print "\b"

board = generate_board(3)
print_board(board)

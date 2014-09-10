import random

def generate_number(start,used):
	size = start ** 2
	new_num = 0
	while new_num in used:
		new_num = random.randint(1,size)
	return new_num

def generate_segment(start,used):
	segment = []
	for index in range(start):
		new_number = generate_number(start,used)
		segment.append(new_number)
		used.append(new_number)
	return segment

def generate_block(start):
	block = []
	used = [0]
	for index in range(start):
		segment = generate_segment(start,used)
		block.append(segment)
		used += segment
	return block

print generate_number(2,[0])
print generate_segment(2,[0])
print generate_block(3)

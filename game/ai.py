import random
from copy import deepcopy

from game.checks import check_winner, check_full


def random_ai(pieces: list[list[list[int]]]) -> (int, int):
	# Play random valid move
	while True:
		x = random.randint(0, 3)
		z = random.randint(0, 3)
		if pieces[x][3][z] == 0:
			return x, z


def ai(pieces: list[list[list[int]]], depth: int) -> (int, int):
	out = recursion(pieces, depth, 2)
	return out[1], out[2]


def recursion(pieces: list[list[list[int]]], depth: int, playing: int) -> (
int, int, int):  # returns (-1 = WIN or X = possible moves, x, z)
	if check_full(pieces):
		return 1, -1, -1
	if depth == 0:
		return 1, -1, -1
	possible = 0
	best_options = []
	best_value = 999999
	# Try all possibilities
	for x in range(4):
		for z in range(4):
			ps = deepcopy(pieces)
			height = -1
			for i in range(4):
				if ps[x][i][z] == 0:
					height = i
					break
			if height < 0:
				continue
			ps[x][height][z] = playing
			# Check if this is a winning move, if so, return it
			w = check_winner(ps)
			if w == playing:
				return -1, x, z
			elif w != 0:
				# We don't want to do a losing move, try other possibilities
				continue
			
			# Recursion (next move is opponent's)
			opponent = recursion(ps, depth - 1, 3 - playing)
			if opponent[0] == -1:
				continue
			if opponent[0] == 0:
				return -1, x, z
			if opponent[1] < best_value:
				best_value = opponent[1]
				best_options = [(x, z)]
			elif opponent[1] == best_value:
				best_options.append((x, z))
			possible += 1
	
	# There are only losing moves, return first valid one
	if len(best_options) == 0:
		for x in range(4):
			for z in range(4):
				ps = deepcopy(pieces)
				height = -1
				for i in range(4):
					if ps[x][i][z] == 0:
						height = i
						break
				if height >= 0:
					return 0, x, z
	
	# Choose randomly from best options
	best_option = random.choice(best_options)
	return possible, best_option[0], best_option[1]

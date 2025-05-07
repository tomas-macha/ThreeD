from copy import deepcopy

from game.checks import check_winner, check_full

def ai(pieces: list[list[list[int]]], depth: int) -> (int, int):
	out = recursion(pieces, depth, 2)
	return out[1], out[2]

def recursion(pieces: list[list[list[int]]], depth: int, playing: int) -> (int, int, int): # returns (-1 = WIN or X = possible moves, x, z)
	if check_full(pieces):
		return 1, -1, -1
	if depth == 0:
		return 1, -1, -1
	possible = 0
	best_option = (0, 0)
	best_value = 999999
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
			w = check_winner(ps)
			if w == playing:
				return -1, x, z
			elif w != 0:
				continue
			
			opponent = recursion(ps, depth-1, 3-playing)
			if opponent[0] == -1:
				continue
			if opponent[0] == 0:
				return -1, x, z
			if opponent[1] < best_value:
				best_value = opponent[1]
				best_option = (x, z)
			possible += 1
			
	if best_value == 999999:
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

	return possible, best_option[0], best_option[1]
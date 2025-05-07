
def check_winner(pieces: list[list[list[int]]]):
	r1 = pieces[0][0][0]
	r2 = pieces[0][0][3]
	r3 = pieces[0][3][0]
	r4 = pieces[0][3][3]
	for i in range(1,4):
		if pieces[i][i][i] != r1:
			r1 = 0
		if pieces[i][i][3-i] != r2:
			r2 = 0
		if pieces[i][3-i][i] != r3:
			r3 = 0
		if pieces[i][3-i][3-i] != r4:
			r4 = 0
	m = max(r1, r2, r3, r4)
	if m > 0:
		return m

	for i in range(4):
		for j in range(4):
			p1 = pieces[i][j][0]
			p2 = pieces[i][0][j]
			p3 = pieces[0][i][j]
			q1 = pieces[i][0][0]
			q2 = pieces[i][0][3]
			q3 = pieces[0][i][0]
			q4 = pieces[0][i][3]
			q5 = pieces[0][0][i]
			q6 = pieces[0][3][i]
			for k in range(1,4):
				if pieces[i][j][k] != p1:
					p1 = 0
				if pieces[i][k][j] != p2:
					p2 = 0
				if pieces[k][i][j] != p3:
					p3 = 0
				if pieces[i][k][k] != q1:
					q1 = 0
				if pieces[i][k][3-k] != q2:
					q2 = 0
				if pieces[k][i][k] != q3:
					q3 = 0
				if pieces[k][i][3-k] != q4:
					q4 = 0
				if pieces[k][k][i] != q5:
					q5 = 0
				if pieces[k][3-k][i] != q6:
					q6 = 0
			m = max(p1, p2, p3, q1, q2, q3, q4, q5, q6)
			if m > 0:
				return m
	return 0

def check_full(pieces: list[list[list[int]]]):
	for i in range(4):
		for j in range(4):
			for k in range(4):
				if pieces[i][j][k] == 0:
					return False
	return True

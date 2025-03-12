class Matrix:
	def __init__(self, rows: int, cols: int, data: list[list[int]]) -> None:
		self.rows = rows
		self.cols = cols
		self.data = data
	
	def __str__(self) -> str:
		return "\n".join([str(row) for row in self.data]) + "\n"
	
	def __add__(self, other: "Matrix") -> "Matrix":
		if self.rows != other.rows or self.cols != other.cols:
			raise ValueError("Matrices must have the same dimensions")
		result = Matrix(self.rows, self.cols, self.data)
		for i in range(self.rows):
			for j in range(self.cols):
				result.data[i][j] += other.data[i][j]
		return result
	
	def __sub__(self, other: "Matrix") -> "Matrix":
		if self.rows != other.rows or self.cols != other.cols:
			raise ValueError("Matrices must have the same dimensions")
		result = Matrix(self.rows, self.cols, self.data)
		for i in range(self.rows):
			for j in range(self.cols):
				result.data[i][j] -= other.data[i][j]
		return result
	
	def __mul__(self, other: "Matrix") -> "Matrix":
		if self.cols != other.rows:
			raise ValueError(
				"Number of columns in the first matrix must be equal to the number of rows in the second matrix")
		result = Matrix(self.rows, other.cols, [[0 for _ in range(other.cols)] for _ in range(self.rows)])
		for i in range(self.rows):
			for j in range(other.cols):
				for k in range(self.cols):
					result.data[i][j] += self.data[i][k] * other.data[k][j]
		return result
	
	def transpose(self) -> "Matrix":
		result = Matrix(self.cols, self.rows, self.data)
		for i in range(self.rows):
			for j in range(self.cols):
				result.data[j][i] = self.data[i][j]
		return result



from math import cos, sin

from matrix import Matrix


class Vertex:
	def __init__(self, x: float, y: float, z: float):
		self.x = x
		self.y = y
		self.z = z
		self.last_rid = -1
		self.rendered_x = 0
		self.rendered_y = 0
	
	def apply(self, matrix: Matrix, rid: int, width: int, height: int, focal: int) -> (int, int, int):
		if rid == self.last_rid:
			return self.rendered_x, self.rendered_y
		xyz = matrix * Matrix(4, 1, [[self.x], [self.y], [self.z], [1]])
		if xyz.data[2][0] <= 0:
			return None, None, None
		x = xyz.data[0][0] * focal / xyz.data[2][0] + width / 2
		y = xyz.data[1][0] * focal / xyz.data[2][0] + height / 2
		self.last_rid = rid
		self.rendered_x = x
		self.rendered_y = y
		#return x, y, xyz.data[0][0] ** 2 + xyz.data[1][0] ** 2 + xyz.data[2][0] ** 2
		z = xyz.data[0][0] ** 2 + xyz.data[1][0] ** 2 + (xyz.data[2][0]) ** 2
		#z = xyz.data[2][0]
		return x, y, z
	
	def __repr__(self):
		return f"Vertex({self.x}, {self.y}, {self.z})"


def neutral() -> Matrix:
	return Matrix(4, 4, [
		[1, 0, 0, 0],
		[0, 1, 0, 0],
		[0, 0, 1, 0],
		[0, 0, 0, 1]
	])

def translate(dx: float, dy: float, dz: float) -> Matrix:
	return Matrix(4, 4, [
		[1, 0, 0, dx],
		[0, 1, 0, dy],
		[0, 0, 1, dz],
		[0, 0, 0, 1]
	])

def rotate_x(theta: float) -> Matrix:
	return Matrix(4, 4, [
		[1, 0, 0, 0],
		[0, cos(theta), -sin(theta), 0],
		[0, sin(theta), cos(theta), 0],
		[0, 0, 0, 1]
	])

def rotate_y(theta: float) -> Matrix:
	return Matrix(4, 4, [
		[cos(theta), 0, sin(theta), 0],
		[0, 1, 0, 0],
		[-sin(theta), 0, cos(theta), 0],
		[0, 0, 0, 1]
	])

def rotate_z(theta: float) -> Matrix:
	return Matrix(4, 4, [
		[cos(theta), -sin(theta), 0, 0],
		[sin(theta), cos(theta), 0, 0],
		[0, 0, 1, 0],
		[0, 0, 0, 1]
	])
from math import cos, sin

from .matrix import Matrix


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


def scale(sx: float, sy: float, sz: float) -> Matrix:
	return Matrix(4, 4, [
		[sx, 0, 0, 0],
		[0, sy, 0, 0],
		[0, 0, sz, 0],
		[0, 0, 0, 1]
	])

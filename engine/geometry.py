from math import ceil
from typing import Callable

from .engine import Triangle, Frame
from .matrix import Matrix
from .utils import Color


class Vertex:
	def __init__(self, x: float, y: float, z: float):
		self.x = x
		self.y = y
		self.z = z
		self.last_rid = -1
		self.rendered_x = 0
		self.rendered_y = 0
		self.rendered_z = 0
	
	# Transform vertex to screen coordinates
	def apply(self, matrix: Matrix, rid: int, width: int, height: int, focal: int) -> (int, int, int):
		if rid == self.last_rid:
			return self.rendered_x, self.rendered_y, self.rendered_z
		xyz = matrix * Matrix(4, 1, [[self.x], [self.y], [self.z], [1]])
		if xyz.data[2][0] <= 0:
			return None, None, None
		x = xyz.data[0][0] * focal / xyz.data[2][0] + width / 2
		y = xyz.data[1][0] * focal / xyz.data[2][0] + height / 2
		z = xyz.data[0][0] ** 2 + xyz.data[1][0] ** 2 + (xyz.data[2][0]) ** 2
		# z = xyz.data[0][0] + xyz.data[1][0] + xyz.data[2][0]
		self.last_rid = rid
		self.rendered_x = x
		self.rendered_y = y
		self.rendered_z = z
		return x, y, z
	
	def __repr__(self):
		return f"Vertex({self.x}, {self.y}, {self.z})"


# Create cube from rectangles (each rectangle is from triangles)
def cube(frame: Frame, x1: float, y1: float, z1: float, x2: float, y2: float, z2: float, color: Color,
         onclick: Callable[[], None] | None = None):
	r1 = rectangle(frame, [
		Vertex(x1, y1, z1),
		Vertex(x2, y1, z1),
		Vertex(x2, y2, z1),
		Vertex(x1, y2, z1),
	], color, onclick)
	r2 = rectangle(frame, [
		Vertex(x1, y1, z1),
		Vertex(x1, y2, z1),
		Vertex(x1, y2, z2),
		Vertex(x1, y1, z2),
	], color, onclick)
	r3 = rectangle(frame, [
		Vertex(x1, y1, z1),
		Vertex(x1, y1, z2),
		Vertex(x2, y1, z2),
		Vertex(x2, y1, z1),
	], color, onclick)
	r4 = rectangle(frame, [
		Vertex(x2, y1, z1),
		Vertex(x2, y2, z1),
		Vertex(x2, y2, z2),
		Vertex(x2, y1, z2),
	], color, onclick)
	r5 = rectangle(frame, [
		Vertex(x1, y2, z1),
		Vertex(x2, y2, z1),
		Vertex(x2, y2, z2),
		Vertex(x1, y2, z2),
	], color, onclick)
	r6 = rectangle(frame, [
		Vertex(x1, y1, z2),
		Vertex(x2, y1, z2),
		Vertex(x2, y2, z2),
		Vertex(x1, y2, z2),
	], color, onclick)
	return r1 + r2 + r3 + r4 + r5 + r6


# Split rectangle into triangles
def rectangle(frame: Frame, vertices: list[Vertex], fill: Color, onclick: Callable[[], None] | None = None):
	v0 = vertices[0]
	v1 = vertices[1]
	v2 = vertices[2]
	v3 = vertices[3]
	a1 = (v0.x - v1.x) ** 2 + (v0.y - v1.y) ** 2 + (v0.z - v1.z) ** 2
	a2 = (v1.x - v2.x) ** 2 + (v1.y - v2.y) ** 2 + (v1.z - v2.z) ** 2
	split1 = ceil(a1 / frame.config.split_quality)
	split2 = ceil(a2 / frame.config.split_quality)
	d1 = Vertex((v1.x - v0.x) / split1, (v1.y - v0.y) / split1, (v1.z - v0.z) / split1)
	d2 = Vertex((v2.x - v1.x) / split2, (v2.y - v1.y) / split2, (v2.z - v1.z) / split2)
	
	triangles: list[Triangle] = []
	
	for i in range(split1):
		for j in range(split2):
			n0 = Vertex(
				v0.x + d1.x * i + d2.x * j,
				v0.y + d1.y * i + d2.y * j,
				v0.z + d1.z * i + d2.z * j
			)
			n1 = Vertex(
				v0.x + d1.x * (i + 1) + d2.x * j,
				v0.y + d1.y * (i + 1) + d2.y * j,
				v0.z + d1.z * (i + 1) + d2.z * j
			)
			n2 = Vertex(
				v0.x + d1.x * (i + 1) + d2.x * (j + 1),
				v0.y + d1.y * (i + 1) + d2.y * (j + 1),
				v0.z + d1.z * (i + 1) + d2.z * (j + 1)
			)
			n3 = Vertex(
				v0.x + d1.x * i + d2.x * (j + 1),
				v0.y + d1.y * i + d2.y * (j + 1),
				v0.z + d1.z * i + d2.z * (j + 1)
			)
			
			t1 = triangle(frame, [n0, n1, n2], fill, onclick)
			t2 = triangle(frame, [n0, n3, n2], fill, onclick)
			triangles.append(t1)
			triangles.append(t2)
	return triangles


def triangle(frame: Frame, vertices: list[Vertex], fill: Color, onclick: Callable[[], None] | None = None):
	color = fill.copy()
	return Triangle(frame, vertices, color, onclick)

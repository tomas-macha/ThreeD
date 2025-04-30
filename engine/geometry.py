from math import cos, sin, radians, ceil
from random import randint
from typing import Callable

from .engine import Triangle, Frame
from .matrices import Vertex
from .utils import rgb, Color

"""
def cube(frame: Frame, x1: float, y1: float, z1: float, x2: float, y2: float, z2: float):
	triangle(frame, [
		Vertex(x1, y1, z1),
		Vertex(x2, y1, z1),
		Vertex(x2, y2, z1),
	], rgb(100, 120, 150))
	
	triangle(frame, [
		Vertex(x1, y1, z1),
		Vertex(x2, y2, z1),
		Vertex(x1, y2, z1),
	], rgb(120, 140, 170))
	
	triangle(frame, [
		Vertex(x1, y1, z1),
		Vertex(x1, y2, z1),
		Vertex(x1, y2, z2),
	], rgb(130, 100, 70))
	
	triangle(frame, [
		Vertex(x1, y1, z1),
		Vertex(x1, y2, z2),
		Vertex(x1, y1, z2),
	], rgb(150, 120, 90))
	
	triangle(frame, [
		Vertex(x1, y1, z1),
		Vertex(x1, y1, z2),
		Vertex(x2, y1, z2),
	], rgb(100, 170, 130))
	
	triangle(frame, [
		Vertex(x1, y1, z1),
		Vertex(x2, y1, z2),
		Vertex(x2, y1, z1),
	], rgb(120, 190, 150))
	
	triangle(frame, [
		Vertex(x2, y1, z1),
		Vertex(x2, y2, z1),
		Vertex(x2, y2, z2),
	], rgb(170, 80, 110))
	
	triangle(frame, [
		Vertex(x2, y1, z1),
		Vertex(x2, y2, z2),
		Vertex(x2, y1, z2),
	], rgb(190, 100, 130))
	
	triangle(frame, [
		Vertex(x1, y2, z1),
		Vertex(x2, y2, z1),
		Vertex(x2, y2, z2),
	], rgb(140, 150, 110))
	
	triangle(frame, [
		Vertex(x1, y2, z1),
		Vertex(x2, y2, z2),
		Vertex(x1, y2, z2),
	], rgb(160, 170, 130))
	
	triangle(frame, [
		Vertex(x1, y1, z2),
		Vertex(x2, y1, z2),
		Vertex(x2, y2, z2),
	], rgb(190, 160, 110))
	
	triangle(frame, [
		Vertex(x1, y1, z2),
		Vertex(x2, y2, z2),
		Vertex(x1, y2, z2),
	], rgb(210, 180, 130))
"""

def cube_from_triangles(frame: Frame, x1: float, y1: float, z1: float, x2: float, y2: float, z2: float, color: Color):
	triangle(frame, [
		Vertex(x1, y1, z1),
		Vertex(x2, y1, z1),
		Vertex(x2, y2, z1),
	], color)
	
	triangle(frame, [
		Vertex(x1, y1, z1),
		Vertex(x2, y2, z1),
		Vertex(x1, y2, z1),
	], color)
	
	triangle(frame, [
		Vertex(x1, y1, z1),
		Vertex(x1, y2, z1),
		Vertex(x1, y2, z2),
	], color)
	
	triangle(frame, [
		Vertex(x1, y1, z1),
		Vertex(x1, y2, z2),
		Vertex(x1, y1, z2),
	], color)
	
	triangle(frame, [
		Vertex(x1, y1, z1),
		Vertex(x1, y1, z2),
		Vertex(x2, y1, z2),
	], color)
	
	triangle(frame, [
		Vertex(x1, y1, z1),
		Vertex(x2, y1, z2),
		Vertex(x2, y1, z1),
	], color)
	
	triangle(frame, [
		Vertex(x2, y1, z1),
		Vertex(x2, y2, z1),
		Vertex(x2, y2, z2),
	], color)
	
	triangle(frame, [
		Vertex(x2, y1, z1),
		Vertex(x2, y2, z2),
		Vertex(x2, y1, z2),
	], color)
	
	triangle(frame, [
		Vertex(x1, y2, z1),
		Vertex(x2, y2, z1),
		Vertex(x2, y2, z2),
	], color)
	
	triangle(frame, [
		Vertex(x1, y2, z1),
		Vertex(x2, y2, z2),
		Vertex(x1, y2, z2),
	], color)
	
	triangle(frame, [
		Vertex(x1, y1, z2),
		Vertex(x2, y1, z2),
		Vertex(x2, y2, z2),
	], color)
	
	triangle(frame, [
		Vertex(x1, y1, z2),
		Vertex(x2, y2, z2),
		Vertex(x1, y2, z2),
	], color)
	
def cube(frame: Frame, x1: float, y1: float, z1: float, x2: float, y2: float, z2: float, color: Color, onclick: Callable[[], None]|None = None):
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
	
def rectangle(frame: Frame, vertices: list[Vertex], fill: Color, onclick: Callable[[], None]|None = None):
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
				v0.x + d1.x*i + d2.x*j,
				v0.y + d1.y*i + d2.y*j,
				v0.z + d1.z*i + d2.z*j
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
	
	
def triangle(frame: Frame, vertices: list[Vertex], fill: Color, onclick: Callable[[], None]|None = None):
	color = fill.copy()
	return Triangle(frame, vertices, color, onclick)

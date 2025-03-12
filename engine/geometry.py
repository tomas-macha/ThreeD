from random import randint

from engine import Triangle, Frame
from matrices import Vertex
from utils import rgb


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


def triangle(frame: Frame, vertices: list[Vertex], fill: str):
	max_size = frame.config.split_quality
	d01 = (vertices[0].x - vertices[1].x) ** 2 + (vertices[0].y - vertices[1].y) ** 2 + (vertices[0].z - vertices[1].z) ** 2
	d12 = (vertices[1].x - vertices[2].x) ** 2 + (vertices[1].y - vertices[2].y) ** 2 + (vertices[1].z - vertices[2].z) ** 2
	d20 = (vertices[2].x - vertices[0].x) ** 2 + (vertices[2].y - vertices[0].y) ** 2 + (vertices[2].z - vertices[0].z) ** 2
	
	if d01 > max_size or d12 > max_size or d20 > max_size:
		c01 = Vertex((vertices[0].x + vertices[1].x) / 2, (vertices[0].y + vertices[1].y) / 2, (vertices[0].z + vertices[1].z) / 2)
		c12 = Vertex((vertices[1].x + vertices[2].x) / 2, (vertices[1].y + vertices[2].y) / 2, (vertices[1].z + vertices[2].z) / 2)
		c20 = Vertex((vertices[2].x + vertices[0].x) / 2, (vertices[2].y + vertices[0].y) / 2, (vertices[2].z + vertices[0].z) / 2)
		triangle(frame, [vertices[0], c01, c20], fill)
		triangle(frame, [vertices[1], c01, c12], fill)
		triangle(frame, [vertices[2], c12, c20], fill)
		triangle(frame, [c01, c12, c20], fill)
	else:
		Triangle(frame, vertices, fill)


def random_color_cube(main, x1: float, y1: float, z1: float, x2: float, y2: float, z2: float):
	Triangle(main, [
		Vertex(x1, y1, z1),
		Vertex(x2, y1, z1),
		Vertex(x2, y2, z1),
	], rgb(randint(0, 255), randint(0, 255), randint(0, 255)))
	
	Triangle(main, [
		Vertex(x1, y1, z1),
		Vertex(x2, y2, z1),
		Vertex(x1, y2, z1),
	], rgb(randint(0, 255), randint(0, 255), randint(0, 255)))
	
	Triangle(main, [
		Vertex(x1, y1, z1),
		Vertex(x1, y2, z1),
		Vertex(x1, y2, z2),
	], rgb(randint(0, 255), randint(0, 255), randint(0, 255)))
	
	Triangle(main, [
		Vertex(x1, y1, z1),
		Vertex(x1, y2, z2),
		Vertex(x1, y1, z2),
	], rgb(randint(0, 255), randint(0, 255), randint(0, 255)))
	
	Triangle(main, [
		Vertex(x1, y1, z1),
		Vertex(x1, y1, z2),
		Vertex(x2, y1, z2),
	], rgb(randint(0, 255), randint(0, 255), randint(0, 255)))
	
	Triangle(main, [
		Vertex(x1, y1, z1),
		Vertex(x2, y1, z2),
		Vertex(x2, y1, z1),
	], rgb(randint(0, 255), randint(0, 255), randint(0, 255)))
	
	Triangle(main, [
		Vertex(x2, y1, z1),
		Vertex(x2, y2, z1),
		Vertex(x2, y2, z2),
	], rgb(randint(0, 255), randint(0, 255), randint(0, 255)))
	
	Triangle(main, [
		Vertex(x2, y1, z1),
		Vertex(x2, y2, z2),
		Vertex(x2, y1, z2),
	], rgb(randint(0, 255), randint(0, 255), randint(0, 255)))
	
	Triangle(main, [
		Vertex(x1, y2, z1),
		Vertex(x2, y2, z1),
		Vertex(x2, y2, z2),
	], rgb(randint(0, 255), randint(0, 255), randint(0, 255)))
	
	Triangle(main, [
		Vertex(x1, y2, z1),
		Vertex(x2, y2, z2),
		Vertex(x1, y2, z2),
	], rgb(randint(0, 255), randint(0, 255), randint(0, 255)))
	
	Triangle(main, [
		Vertex(x1, y1, z2),
		Vertex(x2, y1, z2),
		Vertex(x2, y2, z2),
	], rgb(randint(0, 255), randint(0, 255), randint(0, 255)))
	
	Triangle(main, [
		Vertex(x1, y1, z2),
		Vertex(x2, y2, z2),
		Vertex(x1, y2, z2),
	], rgb(randint(0, 255), randint(0, 255), randint(0, 255)))
	
	
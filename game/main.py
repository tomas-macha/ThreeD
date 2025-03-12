from math import cos, sin
from random import randint

from PyQt5.Qt import Qt

from engine.engine import App, Config, Frame, Transformation
from engine.geometry import cube
from engine.matrices import neutral, translate, rotate_y, rotate_x

app = App(Config(
	title = "3D Engine",
	width = 800,
	height = 600,
	focal = 450,
	split_quality = 750,
	middle_frame=True
))
engine = app.engine


class Camera(Transformation):
	
	def __init__(self):
		super().__init__(neutral())
		self.x = 0
		self.y = 30
		self.z = 100
		self.rx = 0
		self.ry = 0
	
	def generate(self, rid: int):
		if Qt.Key_W in app.keys:
			self.x += sin(self.ry) * 5
			self.z -= cos(self.ry) * 5
		if Qt.Key_S in app.keys:
			self.x -= sin(self.ry) * 5
			self.z += cos(self.ry) * 5
		if Qt.Key_A in app.keys:
			self.x += cos(self.ry) * 5
			self.z += sin(self.ry) * 5
		if Qt.Key_D in app.keys:
			self.x -= cos(self.ry) * 5
			self.z -= sin(self.ry) * 5
		if Qt.Key_E in app.keys:
			self.y += 5
		if Qt.Key_Q in app.keys:
			self.y -= 5
			
		if Qt.Key_Up in app.keys:
			self.rx -= 0.02
		if Qt.Key_Down in app.keys:
			self.rx += 0.02
		if Qt.Key_Right in app.keys:
			self.ry -= 0.05
		if Qt.Key_Left in app.keys:
			self.ry += 0.05
		
		self.matrix = neutral() * rotate_x(self.rx) * rotate_y(self.ry) * translate(self.x, self.y, self.z)
		
class Piece(Transformation):
	
	def __init__(self, x: int, y: int, z: int):
		super().__init__(neutral())
		self.x = x
		self.y = y
		self.z = z
		
		self.moving_y = 5
	
	def generate(self, rid: int):
		if self.moving_y > self.y:
			self.moving_y += (self.y - self.moving_y) * 0.2
		self.matrix = neutral() * translate(self.x*30, -self.moving_y*30, self.z*30) * translate(3, -5, 3)
		

main = Frame(engine, [Camera()])

DARK_BROWN = "#654321"
LIGHT_BROWN = "#987654"

DARK_PIECE = "#A18321"

cube(main, 0, 0, 0, 120, -5, 120, DARK_BROWN)

for x in range(4):
	for y in range(4):
		cube(main, 12+x*30, -5, 12+y*30, 18+x*30, -96, 18+y*30, LIGHT_BROWN)

piece1 = Frame(main, [Piece(0, 0, 0)])

cube(piece1, 0, 0, 0, 24, -24, 24, DARK_PIECE)

app.run()
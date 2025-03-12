from math import cos, sin

from PyQt5.Qt import Qt

from engine import App, Config, Frame, Transformation
from geometry import cube
from matrices import neutral, translate, rotate_y, rotate_x

app = App(Config(
	title = "3D Engine",
	width = 800,
	height = 600,
	focal = 450,
	split_quality = 50,
	middle_frame=True
))
engine = app.engine


class Camera(Transformation):
	
	def __init__(self):
		super().__init__(neutral())
		self.x = -20
		self.y = -20
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
		
		

main = Frame(engine, [Camera()])

for i in range(10):
	cube(main, 0, 0, 0+i*20, 20, 20, 20+i*20)
	
for i in range(10):
	cube(main, 0+i*20, 0+i*20, 0, 20+i*20, 20+i*20, 20)
	
for i in range(10):
	#random_color_cube(main, 100 + i*10, 100 + i*10, 100 + i*10, 105 + i*10, 105 + i*10, 105 + i*10)
	pass

"""
triangle(main, [
	Vertex(0, 0, 0),
	Vertex(0, 20, 0),
	Vertex(20, 0, 0),
], rgb(140, 150, 110))

Triangle(main, [
	Vertex(0, 0, 20),
	Vertex(0, 20, 20),
	Vertex(20, 0, 20),
], rgb(110, 150, 140))
"""
"""
Triangle(main, [
	Vertex(0, 0, 0),
	Vertex(0, 20, 0),
	Vertex(20, 0, 0),
], rgb(140, 150, 110))
"""

"""
Triangle(main, [
	Vertex(0, 00, 0),
	Vertex(20, 00, 0),
	Vertex(20, 00, 20),
], rgb(110, 150, 140))
"""
app.run()
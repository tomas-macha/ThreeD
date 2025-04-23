from math import cos, sin

from PyQt5.Qt import Qt
from PyQt5.QtWidgets import QLabel

from engine.engine import App, Config, Frame, Transformation, Vars, Triangle
from engine.geometry import cube
from engine.matrices import neutral, translate, rotate_y, rotate_x, scale, rotate_z

app = App(Config(
	title = "3D Engine",
	width = 800,
	height = 600,
	focal = 450,
	split_quality = 1000,
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
		if Qt.Key_X in app.keys and (self.x == 0 or self.x == 3 or self.z == 0 or self.z == 3):
			self.matrix = neutral() * scale(0, 0, 0)
			return
			
		if self.moving_y > self.y:
			self.moving_y += (self.y - self.moving_y) * 0.2
		self.matrix = neutral() * translate(self.x*30, -self.moving_y*26, self.z*30) * translate(3, -5, 3)


class Chooser(Transformation):
	
	def __init__(self, camera: Camera):
		super().__init__(neutral())
		self.camera = camera
	
	def generate(self, rid: int):
		
		self.matrix = neutral() * translate(-0.65, -0.5, 0) * scale(0.5, 0.3, 1) * rotate_z(self.camera.ry) * translate(-0.285, -0.285, 0)


camera = Camera()
main = Frame(engine, [camera])

DARK_BROWN = "#654321"
LIGHT_BROWN = "#987654"

DARK_PIECE = "#382a92"
LIGHT_PIECE = "#b8eae3"

# GLOBAL VARIABLES
vrs = Vars()
vrs.pieces = [[[0, 0, 0, 0] for i in range(4)] for j in range(4)]
vrs.playing = 1

# QT FIELDS
message = QLabel("You can play.", app.window)

# GROUND
cube(main, 0, 0, 0, 120, -5, 120, DARK_BROWN)
for x in range(4):
	for y in range(4):
		cube(main, 12+x*30, -5, 12+y*30, 18+x*30, -96, 18+y*30, LIGHT_BROWN)


# CHOOSER
chooser = Frame(engine, [Chooser(camera)])
chooser_cubes: list[Triangle] = []
def new_piece_lambda(x: int, z: int):
	X = int(x)
	Z = int(z)
	return lambda: new_piece_xz(X, Z)
for x in range(4):
	for y in range(4):
		new_piece_listener = new_piece_lambda(x, 3-y)
		triangles = cube(chooser, 0+0.15*x, 0+0.15*y, 0, 0.1+0.15*x, 0.1+0.15*y, 1, LIGHT_PIECE, new_piece_listener)
		chooser_cubes.extend(triangles)


def tick():
	pass

def new_piece_xz(x: int, z: int):
	message.setText("You can play.")
	height = -1
	for i in range(4):
		if vrs.pieces[x][i][z] == 0:
			height = i
			vrs.pieces[x][i][z] = vrs.playing
			break
	if height >= 0:
		if vrs.playing == 1:
			new_piece_xyz(x, height, z, LIGHT_PIECE)
		else:
			new_piece_xyz(x, height, z, DARK_PIECE)
		vrs.playing = 3 - vrs.playing
	else:
		message.setText("You can't play here. Try it again.")
		return
		
	for tr in chooser_cubes:
		if vrs.playing == 1:
			tr.fill = LIGHT_PIECE
		else:
			tr.fill = DARK_PIECE

def new_piece_xyz(x: int, y: int, z: int, color: str):
	frame = Frame(main, [Piece(x, y, z)])
	
	cube(frame, 0, 0, 0, 9, -24, 9, color)
	cube(frame, 15, 0, 0, 24, -24, 9, color)
	cube(frame, 0, 0, 15, 9, -24, 24, color)
	cube(frame, 15, 0, 15, 24, -24, 24, color)

	cube(frame, 15, 0, 0, 9, -24, 9, color)
	cube(frame, 0, 0, 9, 9, -24, 15, color)
	cube(frame, 15, 0, 15, 9, -24, 24, color)
	cube(frame, 15, 0, 9, 24, -24, 15, color)


# RUN
app.tick_callback = tick
app.run()
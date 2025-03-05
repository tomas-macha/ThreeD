from abc import abstractmethod
from tkinter import *
from typing import Callable

from matrices import Vertex, neutral
from matrix import Matrix

import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt

from qt import MainWindow


class Config:
	
	def __init__(self, title: str, width: int, height: int, focal: int) -> None:
		self.title = title
		self.width = width
		self.height = height
		self.focal = focal
		self.polygon_callback: Callable[[[(int, int), (int, int), (int, int)], str], None] = self.no_callback
		
	def no_callback(self, vertices: [(int, int), (int, int), (int, int)], fill: str) -> None:
		pass
		
	def create_polygon(self, vertices: [(int, int), (int, int), (int, int)], fill: str) -> None:
		self.polygon_callback(vertices, fill)
		


class Transformation:
	def __init__(self, matrix: Matrix) -> None:
		self.matrix = matrix
	
	@abstractmethod
	def generate(self, rid: int):
		pass


class Triangle:
	
	def __init__(self, frame: "Frame", vertices: [Vertex, Vertex, Vertex], fill: str) -> None:
		frame.add(self)
		self.vertices = vertices
		self.fill = fill
		self.rendered = [(0, 0, 0), (0, 0, 0), (0, 0, 0)]
		
	def calculate(self, frame: "Frame") -> "Triangle":
		self.rendered = frame.apply_points(self.vertices)
		self.rendered.sort(key=lambda x: x[2])
		return self
		
	def render(self, config: Config) -> None:
		pairs = [(point[0], point[1]) for point in self.rendered]
		config.create_polygon(pairs, fill=self.fill)
			

class Frame:
	def __init__(self, parent: "Engine|Frame", transformations: list[Transformation]) -> None:
		self.transformations: list[Transformation] = transformations
		self.triangles: list[Triangle] = []
		self.sub_frames: list[Frame] = []
		self.superMatrix = neutral()
		self.config = parent.add_frame(self)
		self.rid = -1
	
	def add(self, tr: Triangle):
		self.triangles.append(tr)
	
	def add_frame(self, frame: "Frame") -> Config:
		self.sub_frames.append(frame)
		return self.config
	
	def render(self, rid: int, matrix: Matrix, triangles: list[Triangle]):
		self.rid = rid
		self.superMatrix = matrix
		for t in self.transformations:
			t.generate(rid)
			self.superMatrix = self.superMatrix * t.matrix
		for tr in self.triangles:
			try:
				triangles.append(tr.calculate(self))
			except:
				pass
		for frame in self.sub_frames:
			frame.render(rid, self.superMatrix, triangles)
			
	def apply_point(self, point: Vertex) -> (int, int, int):
		return point.apply(self.superMatrix, self.rid, self.config.width, self.config.height, self.config.focal)

	def apply_points(self, points: list[Vertex]) -> list[(int, int, int)]:
		return [self.apply_point(point) for point in points]
	

class Engine:
	def __init__(self, config: Config):
		self.config = config
		self.transformations: list[Transformation] = []
		self.frames: list[Frame] = []
		self.superMatrix = neutral()
	
	def render(self, rid: int):
		triangles: list[Triangle] = []
		for frame in self.frames:
			frame.render(rid, neutral(), triangles)
		triangles.sort(key=lambda x: x.rendered[0][2], reverse=True)
		triangles.sort(key=lambda x: x.rendered[1][2], reverse=True)
		triangles.sort(key=lambda x: x.rendered[2][2], reverse=True)
		for triangle in triangles:
			triangle.render(self.config)
	
	def add_frame(self, obj: Frame) -> Config:
		self.frames.append(obj)
		return self.config


class App:
	def __init__(self, config: Config) -> None:
		
		self.config = config
		
		self.rid = 0
		
		
		"""self.root = Tk()
		self.root.title(config.title)
		self.root.geometry(f"{config.width}x{config.height}")
		self.canvas = Canvas(self.root, width=config.width, height=config.height, bg="white")
		self.canvas.pack()
		self.config.polygon_callback = lambda vertices, fill: self.canvas.create_polygon(vertices, fill=fill)"""
		
		self.app = QtWidgets.QApplication(sys.argv)
		self.window = MainWindow(config.width, config.height)
		

		self.config.polygon_callback = lambda vertices, fill: self.create_polygon(vertices, fill)
		
		
		self.engine = Engine(self.config)
		
		self.keys = []
		
		#self.root.bind("<KeyPress>", self.key_press)
		#self.root.bind("<KeyRelease>", self.key_release)
	
		self.window.keyPressEvent = self.key_press
		self.window.keyReleaseEvent = self.key_release
	
	def create_polygon(self, vertices: [(int, int), (int, int), (int, int)], fill: str) -> None:
		self.window.draw_polygon(vertices, fill)


	def key_press(self, event):
		self.keys.append(event.key())
		
	def key_release(self, event):
		try:
			self.keys.remove(event.key())
		except:
			pass
	
	def run(self):
		self.window.show()
		timer = QtCore.QTimer()
		timer.timeout.connect(self.tick)
		timer.start(100)
		self.app.exec()
	
		#self.root.after(100, self.tick)
		#self.root.mainloop()
		
	def tick(self):
		self.rid += 1
		self.window.clear()
		#self.canvas.delete("all")
		self.engine.render(self.rid)
		#self.root.after(34, self.tick)
		self.window.label.repaint()
		timer = QtCore.QTimer()
		timer.timeout.connect(self.tick)
		timer.start(100)

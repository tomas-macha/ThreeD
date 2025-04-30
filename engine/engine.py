import sys
from abc import abstractmethod
from tkinter import *
from typing import Callable

from PyQt5 import QtCore, QtWidgets

from .matrices import Vertex, neutral
from .matrix import Matrix
from .qt import MainWindow
from .utils import is_point_in_triangle, Color


class Config:
	
	def __init__(self, title: str, width: int, height: int, focal: int, split_quality: int, middle_frame: bool) -> None:
		self.title = title
		self.width = width
		self.height = height
		self.focal = focal
		self.split_quality = split_quality
		self.middle_frame = middle_frame
		self.polygon_callback: Callable[[[(int, int), (int, int), (int, int)], Color], None] = self.no_callback
	
	def no_callback(self, vertices: [(int, int), (int, int), (int, int)], fill: Color) -> None:
		pass
	
	def create_polygon(self, vertices: [(int, int), (int, int), (int, int)], fill: Color) -> None:
		self.polygon_callback(vertices, fill)


class Transformation:
	def __init__(self, matrix: Matrix) -> None:
		self.matrix = matrix
	
	@abstractmethod
	def generate(self, rid: int):
		pass


class Triangle:
	
	def __init__(self, frame: "Frame", vertices: [Vertex, Vertex, Vertex], fill: Color, onclick: Callable[[], None]|None = None) -> None:
		frame.add(self)
		self.vertices = vertices
		self.fill = fill
		self.rendered = [(0, 0, 0), (0, 0, 0), (0, 0, 0)]
		self.previous = [(0, 0, 0), (0, 0, 0), (0, 0, 0)]
		self.ready = False
		self.z_index = [0, 0, 0]
		self.onclick = onclick
	
	def calculate(self, frame: "Frame") -> "Triangle":
		self.previous = self.rendered.copy()
		self.rendered = frame.apply_points(self.vertices)
		self.z_index = [point[2] for point in self.rendered]
		self.z_index.sort()
		return self
	
	def render(self, config: Config) -> None:
		rendered_pairs = [(point[0], point[1]) for point in self.rendered]
		config.create_polygon(rendered_pairs, fill=self.fill)
	
	def render_middle_frame(self, config: Config):
		previous_pairs = [(point[0], point[1]) for point in self.previous]
		rendered_pairs = [(point[0], point[1]) for point in self.rendered]
		middle_pairs = []
		if not self.ready:
			self.ready = True
			return
		try:
			for i in range(3):
				middle_pairs.append(((previous_pairs[i][0] + rendered_pairs[i][0]) / 2,
				                     (previous_pairs[i][1] + rendered_pairs[i][1]) / 2))
			config.create_polygon(middle_pairs, fill=self.fill)
		except:
			pass


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
		self.triangles: list[Triangle] = []
	
	def render_middle_frame(self, rid: int):
		self.triangles = []
		for frame in self.frames:
			frame.render(rid, neutral(), self.triangles)
		
		#self.triangles.sort(key=lambda x: x.z_index[0], reverse=True)
		#self.triangles.sort(key=lambda x: x.z_index[1], reverse=True)
		#self.triangles.sort(key=lambda x: x.z_index[2], reverse=True)
		self.triangles.sort(key=lambda x: x.z_index[0]+x.z_index[1]+x.z_index[2], reverse=True)
		
		for triangle in self.triangles:
			triangle.render_middle_frame(self.config)
	
	def render(self):
		for triangle in self.triangles:
			triangle.render(self.config)
	
	def add_frame(self, obj: Frame) -> Config:
		self.frames.append(obj)
		return self.config
	
	def click(self, x: int, y: int) -> None:
		for triangle in reversed(self.triangles):
			if triangle.onclick is None:
				continue
			if is_point_in_triangle((x, y), triangle.rendered):
				triangle.onclick()
				return


class App:
	def __init__(self, config: Config) -> None:
		
		self.config = config
		self.tick_callback: Callable[[], None] = lambda : None
		
		self.rid = 0
		
		self.app = QtWidgets.QApplication(sys.argv)
		self.window = MainWindow(config.width, config.height, self)
		
		self.config.polygon_callback = lambda vertices, fill: self.create_polygon(vertices, fill)
		
		self.engine = Engine(self.config)
		
		self.keys = []
		
		self.window.keyPressEvent = self.key_press
		self.window.keyReleaseEvent = self.key_release
	
	def create_polygon(self, vertices: [(int, int), (int, int), (int, int)], fill: Color) -> None:
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
	
	def tick(self):
		self.tick_callback()
		self.rid += 1
		self.window.clear()
		self.engine.render_middle_frame(self.rid)
		self.window.label.repaint()
		timer = QtCore.QTimer()
		if self.config.middle_frame:
			timer.timeout.connect(self.tick_full_frame)
		else:
			timer.timeout.connect(self.tick)
		timer.start(1)
	
	def tick_full_frame(self):
		self.engine.render()
		self.window.label.repaint()
		timer = QtCore.QTimer()
		timer.timeout.connect(self.tick)
		timer.start(1)
	
	def click(self, x: int, y: int):
		self.engine.click(x, y)

class Vars:
	pass
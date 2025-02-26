from abc import abstractmethod
from tkinter import *

from matrices import Vertex, neutral
from matrix import Matrix


class Config:
	
	def __init__(self, title: str, width: int, height: int, focal: int) -> None:
		self.title = title
		self.width = width
		self.height = height
		self.focal = focal
		


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
		
	def render(self, canvas: Canvas, image: PhotoImage) -> None:
		pairs = [(point[0], point[1]) for point in self.rendered]
		canvas.create_polygon(pairs, fill=self.fill, outline="black")
		for i in range(3):
			x1, y1 = pairs[i]
			x2, y2 = pairs[(i + 1) % 3]
			#canvas.create_line(x1, y1, x2, y2, fill=self.fill, width=5)
			

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
	
	def render(self, rid: int, canvas: Canvas, matrix: Matrix, triangles: list[Triangle], image: PhotoImage):
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
			frame.render(rid, canvas, self.superMatrix, triangles, image)
			
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
	
	def render(self, rid: int, canvas: Canvas, image: PhotoImage):
		triangles: list[Triangle] = []
		for frame in self.frames:
			frame.render(rid, canvas, neutral(), triangles, image)
		triangles.sort(key=lambda x: x.rendered[0][2], reverse=True)
		triangles.sort(key=lambda x: x.rendered[1][2], reverse=True)
		triangles.sort(key=lambda x: x.rendered[2][2], reverse=True)
		for triangle in triangles:
			triangle.render(canvas, image)
	
	def add_frame(self, obj: Frame) -> Config:
		self.frames.append(obj)
		return self.config


class App:
	def __init__(self, config: Config) -> None:
		
		self.config = config
		
		self.rid = 0
		
		self.root = Tk()
		self.root.title(config.title)
		self.root.geometry(f"{config.width}x{config.height}")
		
		self.canvas = Canvas(self.root, width=config.width, height=config.height, bg="white")
		self.canvas.pack()
		
		self.image = PhotoImage(width=config.width, height=config.height)
		self.created_image = self.canvas.create_image((config.width/2, config.height/2), image=self.image, state="normal")
		
		self.engine = Engine(self.config)
		
		self.keys = []
		
		self.root.bind("<KeyPress>", self.key_press)
		self.root.bind("<KeyRelease>", self.key_release)
	
	def key_press(self, event):
		self.keys.append(event.keysym)
		
	def key_release(self, event):
		self.keys.remove(event.keysym)
	
	def run(self):
		self.root.after(34, self.tick)
		self.root.mainloop()
		
	def tick(self):
		self.rid += 1
		self.root.after(34, self.tick)
		self.canvas.delete("all")
		self.engine.render(self.rid, self.canvas, self.image)

import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt


class MainWindow(QtWidgets.QMainWindow):
	def __init__(self, width, height):
		super().__init__()
		
		self.label = QtWidgets.QLabel()
		self.canvas = QtGui.QPixmap(width, height)
		self.canvas.fill(Qt.white)
		self.label.setPixmap(self.canvas)
		self.setCentralWidget(self.label)
		self.painter = QtGui.QPainter(self.label.pixmap())
	 
	def clear(self):
		pen = QtGui.QPen()
		pen.setWidth(self.width()+self.height())
		pen.setColor(QtGui.QColor('white'))
		self.painter.setPen(pen)
		self.painter.drawPoint(200, 150)
		
	
	def draw_polygon(self, vertices: [(int, int), (int, int), (int, int)], fill: str) -> None:
		path = QtGui.QPainterPath()
		self.painter.setRenderHint(QtGui.QPainter.RenderHint.Antialiasing)
		self.painter.setBrush(QtGui.QColor(fill))
		self.painter.setPen(QtGui.QColor(fill))
		path.moveTo(vertices[0][0], vertices[0][1])
		path.lineTo(vertices[1][0], vertices[1][1])
		path.lineTo(vertices[2][0], vertices[2][1])
		path.lineTo(vertices[0][0], vertices[0][1])
		self.painter.drawPath(path)


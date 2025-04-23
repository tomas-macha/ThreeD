from PyQt5 import QtGui, QtWidgets
from PyQt5.QtCore import Qt

class MainWindow(QtWidgets.QMainWindow):
	def __init__(self, width, height, app: "App"):
		super().__init__()
		
		self.app = app
		
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
	
	def mousePressEvent(self, event):
		if event.button() == Qt.LeftButton:
			x = event.pos().x()
			y = event.pos().y()
			self.app.click(x, y)
	
	def draw_polygon(self, vertices: [(int, int), (int, int), (int, int)], fill: str) -> None:
		path = QtGui.QPainterPath()
		self.painter.setRenderHint(QtGui.QPainter.RenderHint.Antialiasing)
		self.painter.setBrush(QtGui.QColor(fill))
		self.painter.setPen(QtGui.QColor("black"))
		#self.painter.setPen(QtGui.QColor(Qt.transparent))
		path.moveTo(vertices[0][0], vertices[0][1])
		path.lineTo(vertices[1][0], vertices[1][1])
		path.lineTo(vertices[2][0], vertices[2][1])
		path.lineTo(vertices[0][0], vertices[0][1])
		self.painter.drawPath(path)


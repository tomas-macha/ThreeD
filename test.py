from tkinter import *

class App:
	
	def __init__(self):
		
		self.circle = None
		self.rect = None
		self.root = Tk()
		
		self.canvas = Canvas(self.root, width=400, height=400, bg="white")
		self.canvas.pack()
		
		btn = Button(self.root, text="Vykřičník", command=self.excl_mark)
		btn.pack()
		
		self.root.bind("<space>", self.clr)
		self.root.bind("<Right>", lambda e: self.right())
		self.root.bind("<Left>", lambda e: self.left())
		
		
		
	def excl_mark(self):
		
		self.rect = self.canvas.create_rectangle(150, 50, 250, 250, fill="blue")
		
		self.root.after(1000, self.excl_mark_circle)
		
	def excl_mark_circle(self):
		self.circle = self.canvas.create_oval(150, 275, 250, 375, fill="red")
	
	def clr(self, e):
		self.canvas.delete(self.rect)
		self.canvas.delete(self.circle)
		
	def right(self):
		self.canvas.move(self.rect, 10, 0)
		self.canvas.move(self.circle, 10, 0)
		
	def left(self):
		self.canvas.move(self.rect, -10, 0)
		self.canvas.move(self.circle, -10, 0)

app = App()
mainloop()
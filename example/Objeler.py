class Kare:
	def __init__(self, x,y ,a,fill="black"):
		self.x = x
		self.y = y
		self.a = a 
		self.fill = fill
		
	def draw(self, canvas):
		canvas.create_rectangle(self.x-self.a/2,self.y-self.a/2,self.x+self.a/2,self.y+self.a/2,fill=self.fill)


class Daire:
	def __init__(self, x,y ,a,fill="black"):
		self.x = x
		self.y = y
		self.a = a 
		self.fill = fill
		
	def draw(self, canvas):
		canvas.create_oval(self.x-self.a/2,self.y-self.a/2,self.x+self.a/2,self.y+self.a/2,fill=self.fill)

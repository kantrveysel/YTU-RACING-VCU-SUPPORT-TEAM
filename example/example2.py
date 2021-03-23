import Objeler
from tkinter import Tk, Canvas

x,y = 320,240

root = Tk()
canva = Canvas(root, width = 640, height = 480, bg="white")
canva.pack()

mykare = Objeler.Kare(150,200,32)
mydaire = Objeler.Daire(200,150,32,"#090909")

def draw():
	canva.delete("all")
	canva.create_oval(x-16,y-16,x+16,y+16)
	mykare.draw(canva)
	mydaire.draw(canva)
	root.after(5, draw)

def loop():
	root.after(50, loop)

def mouseclick(mouse):
	global x,y
	x = mouse.x
	y = mouse.y
	

draw()
loop()

root.bind("<Button-1>",mouseclick)

root.mainloop()
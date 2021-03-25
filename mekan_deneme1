from tkinter import *
import random
import time
    
class Ball: 
    def __init__(self,canvas,color): 
        self.canvas=canvas 
        self.id=canvas.create_oval(20,20,40,40,fill=color) 
        
        
        starting_position=[-3,-2,-1,1,2,3] 
        random.shuffle(starting_position) 
        self.x = starting_position[0] 
        self.y = 2
        self.canvas_height=self.canvas.winfo_height()
        self.canvas_width=self.canvas.winfo_width() 

    def draw(self): 
        self.canvas.move(self.id,self.x,self.y) 
        pos=self.canvas.coords(self.id) 
        

        if pos[1] <=0: 
            self.y=6 
        if pos[3] >=self.canvas_height: 
            self.y=-6
       
        if pos[0] <=0:
            self.x=6
        if pos[2]>=self.canvas_width:
            self.x=-6
        

def main():
    tk=Tk()
    tk.title("PingPong Game")
    canvas=Canvas(tk,bg="black",width=600,height=400)
    canvas.pack()
    tk.update()

    ball=Ball(canvas,'pink')
    while 1:
        tk.update()
        ball.draw() 
        time.sleep(0.02)
        
main()

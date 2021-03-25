from tkinter import *
import time

pencere=Tk()
my_canvas = Canvas(pencere, height="400", bg="black", width="500", )
my_canvas.pack()
ball = my_canvas.create_oval(10, 10, 50, 50, fill='yellow')
xspeed = yspeed = 10
sayac=0
x=240
y=0
WIDTH, HEIGHT = 500, 400

#SPECİAL 1
engel = my_canvas.create_rectangle(x, y, x + 20, y + 500, fill="blue")

while True:
    #DENEME AMAÇLI TOP HAREKETİ
    my_canvas.move(ball,xspeed,yspeed)
    position=my_canvas.coords(ball)#sol ,üst ,sağ ,alt
    if position[0]<=0 or position[2]>=500:
        xspeed=-xspeed
        sayac=sayac+1
    if position[1] <= 0 or position[3] >= 400:
        yspeed = -yspeed
    # SPECİAL1 ENGELDEN SEKECEK
    if sayac ==1:
        my_canvas.itemconfig(engel,fill="red")
        if position[0] <= 250 and position[2] >= 200 and xspeed<=0:
            xspeed = -xspeed
            sayac = sayac + 1
        if position[2] <= 250 and position[0] >= 200 and xspeed>=0:
            xspeed = -xspeed
            sayac = sayac + 1

    if sayac==3:
        #my_canvas.delete(engel)
        my_canvas.itemconfig(engel,fill="blue")

    #SPECİAL2 HIZLANACAK
    if sayac==4 and xspeed>=0:
        xspeed=50
    if sayac==4 and xspeed<=0:
        xspeed=-50
    #NORMALE DÖNECEK
    if sayac==8 and position[0]>=250 and xspeed>0:
        xspeed=6
    if sayac == 8 and position[2] >= 250 and xspeed < 0:
        xspeed = -6
    if sayac==12:
        sayac=0

    pencere.update()
    time.sleep(0.1)





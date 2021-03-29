import tkinter as tk
import time
import keyboard

pencere= tk.Tk()
my_canvas = tk.Canvas(pencere, height="400", bg="black", width="500", )
my_canvas.pack()
x=240
y=0

#sol ,üst ,sağ ,alt
engel = my_canvas.create_rectangle(x, y, x + 20, y + 500, fill="black")
ball = my_canvas.create_oval(10, 10, 50, 50, fill='yellow')
raket1= my_canvas.create_rectangle(470,170 ,490, 250, fill="blue")
raket2= my_canvas.create_rectangle(20,170 ,40, 250, fill="blue")

boost=my_canvas.create_text(450,15,text="BOOOOST",fill="black")
stop=my_canvas.create_text(40,15,text="BARRİER",fill="black")
invisible=my_canvas.create_text(450,385,text="İNVİSİBLE BALL",fill="black")
invisible_raket=my_canvas.create_text(60,385,text="İNVİSİBLE RACKET", fill="black")


xspeed = 40
yspeed = 10
sayac=0
WIDTH, HEIGHT = 500, 400

#SPECİAL 1
a = -10
while True:
    if keyboard.is_pressed('up'):
        my_canvas.move(raket1, 0, -15)
    if keyboard.is_pressed('down'):
        my_canvas.move(raket1, 0, 15)

    #DENEME AMAÇLI TOP HAREKETİ
    position=my_canvas.coords(ball)
    ball_t_1_lat = position[0]
    ball_t_1_lon = position[1]
    my_canvas.move(ball,xspeed,yspeed)
    position=my_canvas.coords(ball)
    ball_t_2_lat = position[0]
    ball_t_2_lon = position[1]
    


    #my_canvas.move(raket2, 0, a)
    #sol ,üst ,sağ ,alt
    
    if position[0]<=0 or position[2]>=500:
        xspeed=-xspeed
        sayac=sayac+1
    if position[1] <= 0 or position[3] >= 400:
        yspeed = -yspeed


    # SPECİAL1 ENGELDEN SEKECEK
    if sayac ==2 or sayac==13:
        my_canvas.itemconfig(engel,fill="red")
        my_canvas.itemconfig(stop,fill="magenta")
        if position[0] <= 250 and position[2] >= 200 and xspeed<=0:
            xspeed = -xspeed
            sayac = sayac + 1
        if position[2] <= 250 and position[0] >= 200 and xspeed>=0:
            xspeed = -xspeed
            sayac = sayac + 1

    if sayac==3 or sayac==14:
        #my_canvas.delete(engel)
        my_canvas.itemconfig(engel,fill="black")
        my_canvas.itemconfig(stop,fill="black")
    #SPECİAL2 HIZLANACAK
    if sayac==4 and xspeed>=0  or sayac==15 and xspeed>=0:
        xspeed=60
        my_canvas.itemconfig(ball,fill="red")
        my_canvas.itemconfig(boost,fill="magenta")

    if sayac==4 and xspeed<=0 or sayac==15 and xspeed<=0:
        xspeed=-60
        my_canvas.itemconfig(ball,fill="red")
        my_canvas.itemconfig(boost,fill="magenta")

    #NORMALE DÖNECEK
    if sayac==6 and position[0]>=250 and xspeed>0 or sayac==17 and position[0]>=250 and xspeed>0 :
        xspeed=30
        my_canvas.itemconfig(ball,fill="yellow")
        my_canvas.itemconfig(boost,fill="black")

    if sayac == 6 and position[2] <= 250 and xspeed < 0 or sayac==17 and position[0]>=250 and xspeed<0 :
        xspeed = -30
        my_canvas.itemconfig(ball,fill="yellow")
        my_canvas.itemconfig(boost,fill="black")
        


    #TOPU GÖRÜNMEZ YAP, GOLE VE RAKKETTEN SEKMESİNE GÖRE YENİDEN AYARLANACAK
    if sayac==8 or sayac==19:
        my_canvas.itemconfig(ball,fill="black")
        my_canvas.itemconfig(invisible,fill="magenta")

    #TOP NORMALDE DÖNER
    if sayac==9 or sayac==20:
        my_canvas.itemconfig(ball,fill="yellow")
        my_canvas.itemconfig(invisible,fill="black")


    #RAKETLERİ GÖRÜNMEZ YAP
    if sayac==11 and xspeed<=0 :
        my_canvas.itemconfig(raket2,fill="black")
        my_canvas.itemconfig(invisible_raket,fill="magenta")
    if sayac == 11 and xspeed >= 0:
        my_canvas.itemconfig(raket1,fill="black")
        my_canvas.itemconfig(invisible_raket,fill="magenta")
    if sayac==22 and xspeed>=0:
        my_canvas.itemconfig(raket1,fill="black")
        my_canvas.itemconfig(invisible_raket,fill="magenta")
    if  sayac==22 and xspeed<=0:
        my_canvas.itemconfig(raket2,fill="black")
        my_canvas.itemconfig(invisible_raket,fill="magenta")

    if sayac==12 or sayac==23:
        my_canvas.itemconfig(raket1,fill="blue")
        my_canvas.itemconfig(raket2,fill="blue")
        my_canvas.itemconfig(invisible_raket,fill="black")

    if sayac==25:
        sayac=0

    pencere.update()
    time.sleep(0.1)
    #a = a/1.1
    #print(position)
    print(my_canvas.coords(raket2)[0], my_canvas.coords(raket2)[1])
    print("Yatay", ball_t_1_lat, ball_t_2_lat)
    print("Dikey", ball_t_1_lon, ball_t_2_lon)

    lat_egim = ball_t_2_lat - ball_t_1_lat
    lon_egim = ball_t_2_lon - ball_t_1_lon
    egim = lon_egim/lat_egim
    intercept = ball_t_2_lon - (egim * ball_t_2_lat)
    ball_hit = intercept
    
    # -30 ve + 30 olan değerler azaltılarak rakibin seviyesi düşürülebilir.
    print("AI!")
    if intercept < my_canvas.coords(raket2)[1]:
        my_canvas.move(raket2, 0, -30)
    else:
        my_canvas.move(raket2, 0, 30)

    #if my_canvas.coords(raket2)[1] == intercept:
        #my_canvas.move(raket2, 0, 0)
    


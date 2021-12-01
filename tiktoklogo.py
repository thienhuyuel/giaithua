#logo tóp tóp
from turtle import *
speed(1)
width(20)
bgcolor('black')
colors=['#ee1d52', '#69c9d0', 'white']
pos=[(0,0),(-5,13),(-5,6)]
for (x,y),col in zip(pos,colors):
	up()
	goto(x,y)
	down()
	color(col)
	left(180)
	circle(50,270)
	forward(120)
	left(180)
	circle(50,90)
mainloop()
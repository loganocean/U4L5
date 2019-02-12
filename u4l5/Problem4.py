from turtle import *

bob = Turtle()

bob.color("blue")
bob.pensize(3)
bob.speed(0)
bob.shape("turtle")

def drawhex(side):
	for x in range(6):
		bob.forward(side)
		bob.left(60)

for y in range(25,150,25):
	drawhex(y)

mainloop()
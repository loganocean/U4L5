from turtle import *

bob = Turtle()

bob.color("blue")
bob.pensize(5)
bob.speed(0)
bob.shape("turtle")

def drawtriangle():
	for x in range(3):
		bob.forward(100)
		bob.left(120)

drawtriangle()

for x in range(12):
	drawtriangle()
	bob.left(30)

mainloop()
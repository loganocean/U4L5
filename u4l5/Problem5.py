from turtle import *

bob = Turtle()

bob.color("blue")
bob.pensize(3)
bob.speed(3)
bob.shape("turtle")

def drawstar():
	for x in range(5):
		bob.forward(50)
		bob.left(144)

drawstar()

mainloop()
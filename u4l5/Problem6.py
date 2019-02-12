from turtle import *

bob = Turtle()

bob.color("pink")
bob.pensize(3)
bob.speed(0)
bob.shape("turtle")

def drawstar():
	for x in range(5):
		bob.forward(50)
		bob.left(144)

for y in range(2):
	drawstar()
	bob.penup()
	bob.forward(50)
	bob.pendown()

drawstar()

mainloop()
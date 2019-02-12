from turtle import *

bob = Turtle()

bob.color("purple")
bob.pensize(3)
bob.speed(0)
bob.shape("turtle")

def drawstar():
	for x in range(5):
		bob.forward(50)
		bob.left(144)

def row():
	for y in range(3):
		drawstar()
		bob.penup()
		bob.forward(60)
		bob.pendown()

for z in range(4):
	row()
	bob.penup()
	bob.backward(180)
	bob.right(90)
	bob.forward(60)
	bob.left(90)
	bob.pendown()

mainloop()

#bob.write('hello logan')
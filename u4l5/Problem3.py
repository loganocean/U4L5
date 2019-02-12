from turtle import *

bob = Turtle()

bob.color("blue")
bob.pensize(5)
bob.speed(5)
bob.shape("turtle")

for x in range(6):
	bob.forward(100)
	bob.left(60)

mainloop()
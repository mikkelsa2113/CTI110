import turtle
wn = turtle.Screen()
tut = turtle.Turtle()

numSQ = int(0)
numTR = int(0)

tut.backward(50)

while numSQ != 4:
	tut.forward(100)
	tut.left(90)
	numSQ += 1

tut.penup()
tut.forward(25)
tut.left(90)
tut.forward(25)
tut.right(90)
tut.pendown()

while numTR != 3:
	tut.forward(50)
	tut.left(120)
	numTR += 1


wn.mainloop()
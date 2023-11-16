import turtle
wn = turtle.Screen()
tut = turtle.Turtle()

tut.pensize(4)
tut.pencolor('purple')

tut.penup()
tut.backward(100)
tut.pendown()

#A
tut.left(75)
tut.forward(70)
tut.right(150)
tut.forward(35)
tut.right(105)
tut.forward(18)
tut.left(180)
tut.forward(18)
tut.right(75)
tut.forward(35)

tut.penup()
tut.left(75)
tut.forward(50)
tut.pendown()

#M
tut.left(85)
tut.forward(65)
tut.right(140)
tut.forward(40)
tut.left(110)
tut.forward(40)
tut.right(140)
tut.forward(65)

wn.mainloop()
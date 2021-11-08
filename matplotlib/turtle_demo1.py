import turtle

turtle=turtle.Turtle()
screen=turtle.getscreen()

turtle.color('red', 'yellow')
turtle.begin_fill()
for i in range(50):
    turtle.forward(200)
    turtle.left(170)
turtle.end_fill()
screen.mainloop()
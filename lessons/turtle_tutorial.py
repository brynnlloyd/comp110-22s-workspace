"""Turtle Tutorial."""


from turtle import Turtle, colormode, done
leo: Turtle = Turtle()

colormode(255)
leo.color(127, 127, 127)
# leo.color("blue", "yellow")

# leo.speed(50)

leo.penup()
leo.goto(-100, 0)
leo.pendown()

side_length: float = 300.0

leo.begin_fill()
i: int = 0
while (i < 3):
    leo.forward(200)
    leo.left(120)
    i = i + 1
leo.end_fill()
leo.hideturtle()


done()

bob: Turtle = Turtle()

bob.speed(60)
bob.color(19, 19, 19)
bob.penup()
bob.goto(-100, 0)
bob.pendown()


i: int = 0
while (i < 3):
    side_length = side_length * 0.97
    bob.forward(side_length)
    bob.left(120)
    i = i + 1
bob.end_fill()
bob.hideturtle()

"""EX04 - Watching the stars w my favorite person."""

__author__ = "730232367"

from turtle import Turtle, done 
import turtle
from random import randint


def main() -> None:
    """The entrypoint of my scene."""
    Jess: Turtle = Turtle()
    Jess.speed(100)
    Jess.color("white")  # The stars are white
    Nick: Turtle = Turtle()
    Nick.color("grey")  # The moon is grey
    Winston: Turtle = Turtle()
    Winston.color("white")  # The stick figure outline is white
    Schmidt: Turtle = Turtle()
    Schmidt.color("white")  # The other stick figure outline is white
    number_of_stars = 0
    while number_of_stars < 25:  # Draw 25 stars on the screen
        x = randint(-300, 300)
        y = randint(0, 300)
        draw_star(Jess, x, y, 10)  # Width of 10 to make the stars small
        number_of_stars += 1
    draw_moon(Nick, -180, 180, 50)  # Draw the moon in the sky
    draw_head(Winston, -50, -150, 30)  # From here down to the rest of this function draws the two people sitting down
    draw_head(Schmidt, 50, -150, 30)
    draw_body(Winston, -50, -150)
    draw_body(Schmidt, 50, -150)
    draw_left_arm(Winston, -50, -175)
    draw_left_arm(Schmidt, 50, -175)
    draw_right_arm(Winston, -50, -175)
    draw_right_arm(Schmidt, 50, -175)
    draw_left_leg(Winston, -50, -240)
    draw_left_leg(Schmidt, 50, -240)
    draw_right_leg(Winston, -50, -240)
    draw_right_leg(Schmidt, 50, -240)
    done()


turtle.Screen().bgcolor("black")  # Background color is black for night sky


def draw_star(star_turtle: Turtle, x: float, y: float, width: float) -> None:
    """Draw a star of the given width which starts at point x, y."""
    star_turtle.penup()
    star_turtle.goto(x, y)
    star_turtle.setheading(0.0)
    star_turtle.pendown()
    star_turtle.begin_fill()
    i: int = 0
    while i < 5:
        star_turtle.forward(width)
        star_turtle.left(145)
        i = i + 1
    star_turtle.end_fill()
    star_turtle.hideturtle()


def draw_moon(moon_turtle: Turtle, x: float, y: float, radius: float) -> None:
    """Draw a moon of the given width whose diameter is specified by x."""
    moon_turtle.penup()
    moon_turtle.goto(x, y)
    moon_turtle.pendown()
    moon_turtle.begin_fill()
    moon_turtle.circle(radius)  # Useful function that inputs what the radius of the circle is and will draw it for you
    moon_turtle.end_fill()
    moon_turtle.hideturtle()


def draw_head(head_turtle: Turtle, x: float, y: float, radius: float) -> None:
    """Draw the stick figures head in the photo."""
    head_turtle.penup()
    head_turtle.goto(x, y)
    head_turtle.pendown()
    head_turtle.circle(radius)
    head_turtle.hideturtle()


def draw_body(body_turtle: Turtle, x: float, y: float) -> None:
    """Draw the stick figures bodies in the photo."""
    body_turtle.penup()
    body_turtle.goto(x, y)
    body_turtle.pendown()
    body_turtle.left(270)
    body_turtle.forward(90)
    body_turtle.hideturtle()


def draw_left_arm(left_arm_turtle: Turtle, x: float, y: float) -> None:
    """Draw the stick figures left arm in the photo."""
    left_arm_turtle.penup()
    left_arm_turtle.goto(x, y)
    left_arm_turtle.pendown()
    left_arm_turtle.left(-60)
    left_arm_turtle.forward(40)
    left_arm_turtle.hideturtle()


def draw_right_arm(right_arm_turtle: Turtle, x: float, y: float) -> None:
    """Draw the stick figures right arm in the photo."""
    right_arm_turtle.penup()
    right_arm_turtle.towards(0, 0)
    right_arm_turtle.goto(x, y)
    right_arm_turtle.pendown()
    right_arm_turtle.left(-30)
    right_arm_turtle.forward(40)
    right_arm_turtle.hideturtle()


def draw_left_leg(left_leg_turtle: Turtle, x: float, y: float) -> None:
    """Draw the stick figures left leg in the photo."""
    left_leg_turtle.penup()
    left_leg_turtle.goto(x, y)
    left_leg_turtle.pendown()
    left_leg_turtle.left(-60)
    left_leg_turtle.forward(40)
    left_leg_turtle.hideturtle()


def draw_right_leg(right_leg_turtle: Turtle, x: float, y: float) -> None:
    """Draw the stick figures right leg in the photo."""
    right_leg_turtle.penup()
    right_leg_turtle.towards(0, 0)
    right_leg_turtle.goto(x, y)
    right_leg_turtle.pendown()
    right_leg_turtle.left(-90)
    right_leg_turtle.forward(40)
    right_leg_turtle.hideturtle()


if __name__ == "__main__":
    main()
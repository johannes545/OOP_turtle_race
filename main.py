from turtle import Turtle, Screen
import random

screen = Screen()
is_race_on = False
screen.setup(width=500, height=400)
bet = screen.textinput("Make your bet", "which turtle will win the race? enter a color")

jimmy = Turtle(shape="turtle")
timmy = Turtle(shape="turtle")
joey = Turtle(shape="turtle")
moe = Turtle(shape="turtle")
trayce = Turtle(shape="turtle")
kim = Turtle(shape="turtle")

turtles = [jimmy, timmy, joey, moe, trayce, kim]

for turtle in turtles:
    turtle.penup()

jimmy.color("red")
timmy.color("blue")
joey.color("yellow")
moe.color("green")
trayce.color("purple")
kim.color("orange")

jimmy.goto(x=-230,y=-80)
timmy.goto(x=-230, y=-50)
joey.goto(x=-230, y=-20)
moe.goto(x=-230, y=10)
trayce.goto(x=-230, y=40)
kim.goto(x=-230, y=70)

if bet:
    is_race_on = True

while is_race_on:

    for turtle in turtles:
        if turtle.xcor() > 230:
            winning_color = turtle.pencolor()
            if winning_color == bet:
                print(f"Congratz, you won the bet. the winning turtle was the color {winning_color}")
                is_race_on = False
            else:
                print(f"sadly you bet wrong. the winning color was {winning_color}")
                is_race_on = False
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

screen.exitonclick()
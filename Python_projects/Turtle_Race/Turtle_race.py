import random
from turtle import Turtle, Screen
screen = Screen()

screen.setup(width=500,height=400)
user_bet=screen.textinput(title="Make your bet",prompt="Guess Which turtle will win the race? Enter color: ")

default_turtle = Turtle()
default_turtle.hideturtle()

colors = ["red", "green", "blue", "orange", "purple", "yellow"]

start_y=-100
turtles = []
is_race_on = False

for color in colors:
    tim = Turtle(shape="turtle")
    tim.color(color)
    tim.penup()
    tim.goto(x=-240, y=start_y)
    start_y += 40  # Adjust the y position for the next turtle
    turtles.append(tim)

if user_bet:
    is_race_on=True

while is_race_on:
    for turtle in turtles:
        if turtle.xcor()>240:
                is_race_on=False
                winning_color=turtle.pencolor()
                if winning_color==user_bet:
                    print(f"You won!! {winning_color} turtle is winner")
                else:
                    print(f"you loss the game {winning_color} color is winner")

        ran_distance=random.randint(0,10)
        turtle.forward(ran_distance)

screen.exitonclick()
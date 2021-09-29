import random
from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle win the race? Select the color:")
print(f"You made a bet on {user_bet} color turtle")

is_race_on = False
turtles = []
colors = ["red", "orange", "yellow", "green", "blue", "purple"]

for i in range(0, 6):
    tim = Turtle(shape="turtle")
    tim.penup()
    tim.color(colors[i])
    tim.goto(x=-230, y=(2.5 - i) * 50)
    turtles.append(tim)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            if turtle.pencolor() == user_bet:
                print(f"You won! {turtle.pencolor()} win the race.")
            else:
                print(f"You lost! {turtle.pencolor()} win the race.")

        random_distance = random.randint(1, 10)
        turtle.forward(random_distance)
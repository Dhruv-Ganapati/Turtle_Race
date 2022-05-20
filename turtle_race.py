from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=900, height=600)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Name the color: ")
print(user_bet)
colors = ("red", "green", "black", "purple", "blue", "yellow")
y_pos = [-270, -180, -90, 0, 90, 180]
all_turtle = []

for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.speed("fast")
    new_turtle.turtlesize(2)
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-300, y=y_pos[turtle_index])
    all_turtle.append(new_turtle)


if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtle:
        if turtle.xcor() > 300:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The winning turtle is {winning_color} turtle.")
            else:
                print(f"You've lost! The winning turtle is {winning_color} turtle.")
        rand_move = random.randint(0, 10)
        turtle.forward(rand_move)

screen.exitonclick()
# setup: - Set up width and height of the screen.
# textinput: - To show popUp like dialog window for input of a string.
# goto(): - The turtle will move at the position of x and y on graph,
# penup(): - PenUp means to hide th pen
# all_turtle: - appends all the new_turtle into a list.

# from turtle import Turtle, Screen
#
# tim = Turtle()
#
#
#
# def move_forwards():
#     tim.forward(10)
# def move_backward():
#     tim.backward(10)
# def turn_left():
#    new_heading = tim.heading() - 10
#    tim.setheading(new_heading)
# def turn_right():
#    new_heading = tim.heading() + 10
#    tim.setheading(new_heading)
#
# def clear_drawing():
#     tim.clear()
#     tim.penup()
#     tim.home()
#     tim.pendown()
#
#
# screen = Screen()
# screen.listen()
# screen.onkey(key="w", fun=move_forwards)
# screen.onkey(key="s", fun=move_backward)
# screen.onkey(key="d", fun=turn_right)
# screen.onkey(key="a", fun=turn_left)
# screen.onkey(key="c", fun=clear_drawing)
# screen.exitonclick()

from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
is_race_on = False
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race. Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-100, -60, -20, 20, 60, 100]
all_turtles = []
for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_positions[turtle_index])
    all_turtles.append(new_turtle)
if user_bet:
    is_race_on = Turtle
while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! {winning_color} turtle is the winner!")
            else:
                print(f"Sorry! You've lost. {winning_color} turtle is the winner!")
        step = random.randint(0, 10)
        turtle.forward(step)

screen.exitonclick()

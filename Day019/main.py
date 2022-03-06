import turtle as t 
from turtle import Screen
import random

screen = Screen()

nbr_of_racing_turtles = 6
y_axis = -100
x_axis = -230
distance_btn_turtles = 40
racing_turtles_list =[]
colors =["red", "green", "orange", "blue", "purple", "pink"]

screen.setup(width = 500, height= 400)
user_bet = screen.textinput(title = "Make your bet? ", prompt = "Which turtle will win the race? Enter a color: ")

for index in range(0,6):
    my_turtle = t.Turtle(shape = "turtle")
    my_turtle.color(colors[index])
    my_turtle.penup()
    my_turtle.goto(x= x_axis, y= y_axis)
    racing_turtles_list.append(my_turtle)
    y_axis += distance_btn_turtles

if user_bet:
    is_race = True

while is_race:
    for racing_turtle in racing_turtles_list:
        racing_turtle.forward(random.randint(0,10))
        if racing_turtle.xcor() > 220:
            is_race = False
            if user_bet == racing_turtle.color()[0]:
                print("You win")
            else:
                print("you lose")
            print(f"the winner is : { racing_turtle.color()[0] }")
            
                

screen.exitonclick()

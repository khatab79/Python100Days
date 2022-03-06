# import colorgram
# # $ pip install colorgram.py

# def extract_colors(img, numbers_colors):
    
#     colors = colorgram.extract(img, numbers_colors)
#     _colors =[]
#     for color in colors:
#         _colors.append((color.rgb.r, color.rgb.g, color.rgb.b))
#     return _colors

# new_list_colors = extract_colors('Day018\image.jpg', 30)

# print(new_list_colors)

colors = [(240, 245, 241), (236, 239, 243), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102)]


import turtle as t 
from turtle import Screen
import random

t.colormode(255)

timmy = t.Turtle()

timmy.hideturtle()
timmy.penup()
timmy.speed(0)

timmy.setheading(225)
timmy.forward(300)
timmy.setheading(0)

nbr_of_dots = 100

def random_color():
    color = (random.choice(colors))
    return color


for line in range(1, nbr_of_dots + 1):       
    timmy.dot(20,random_color())
    timmy.forward(50)
    
    if line % 10 == 0:
        timmy.setheading(90)
        timmy.forward(50)
        timmy.setheading(180)
        timmy.forward(500)
        timmy.setheading(0)


s = Screen()   
s.exitonclick()  
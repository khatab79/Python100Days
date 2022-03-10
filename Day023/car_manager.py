import random
from turtle import Turtle


COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 0.8

class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.cars = []
        self.hideturtle()
        self.speed_level = 0.1

    def make(self):
        chance = random.randint(0,5)
        if chance == 1:
            color = random.choice(COLORS)
            car = Turtle("square")
            car.shape("square")
            car.color(color)
            car.shapesize(stretch_len= 2, stretch_wid= 1)
            car.penup()
            y_axis = random.randint(-230, 250)
            while car.ycor() == y_axis:
                y_axis = random.randint(-230, 250)
            car.goto(280, y_axis )
            self.cars.append(car)
        
    def move(self):        
        for car in self.cars :  
            car.setheading(180)          
            car.forward(STARTING_MOVE_DISTANCE)

    def level_up(self):
        self.speed_level *= MOVE_INCREMENT

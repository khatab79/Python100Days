from turtle import Turtle, right

DISTANCE = 10

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.x_move = DISTANCE
        self.y_move = DISTANCE 
        self.speed_ball = 0.1
        self.shape("circle")
        self.penup()
        self.color("white")    

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1
        self.speed_ball *= 0.9 

    def reset_position(self):
        self.goto(0,0)
        self.speed_ball = 0.1
        self.bounce_x()
        

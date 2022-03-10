from turtle import Turtle


STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

UP= 90
DOWN = 270

class Player(Turtle):
    def __init__(self) :
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.replay()
        self.left(90)
    
    def move_up(self):
        self.forward(MOVE_DISTANCE)
    
    def move_down(self):
        if self.ycor() > -280:
            self.back(MOVE_DISTANCE)

    def replay(self):
        self.clear()
        self.goto(STARTING_POSITION)
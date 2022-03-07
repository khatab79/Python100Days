from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), ( -40, 0)]

DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    
    def __init__(self):
        self.segments = []        
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for postion in STARTING_POSITIONS:
            new_segment = Turtle("square")
            new_segment.color("white")
            new_segment.penup()
            new_segment.goto(postion)
            self.segments.append(new_segment)

    def move(self):
        _start = len(self.segments) - 1
        _stop  = 0
        _step  = -1

        for seg_nbr in range(_start , _stop, _step ):
            new_x = self.segments[seg_nbr - 1].xcor()
            new_y = self.segments[seg_nbr - 1].ycor()
            self.segments[seg_nbr].goto(new_x, new_y)
        self.head.forward(DISTANCE)

    def up(self):  
        if self.head.heading() != DOWN:      
            self.head.setheading(UP)
    
    def down(self):         
        if self.head.heading() != UP:   
            self.head.setheading(DOWN)

    def left(self):     
        if self.head.heading() != RIGHT:   
            self.head.setheading(LEFT)

    def right(self):      
        if self.head.heading() != LEFT:  
            self.head.setheading(RIGHT)

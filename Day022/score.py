from turtle import Turtle

ALIGNMENT = "center"
FONT = ('Arial', 50, "normal")

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.l_score = 0
        self.r_score = 0
        self.hideturtle()
        self.penup() 
        self.color("white")
        self.display_score()
        
    def display_score(self):   
        self.clear() 
        self.goto(-100, 200)       
        self.write(self.l_score , align= ALIGNMENT, font= FONT)
        self.goto(100, 200)       
        self.write(self.r_score , align= ALIGNMENT, font= FONT)
    
    def increase_score_l(self):
        self.l_score += 1    
        self.display_score()
    
    def increase_score_r(self):
        self.r_score += 1    
        self.display_score()


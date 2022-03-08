from turtle import Turtle

ALIGNMENT = "center"
FONT = ('Arial', 20, "normal")

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.penup() 
        self.color("white")
        self.goto(0, 250)
        self.display_score()
        
    def display_score(self):       
        self.write(f"Score :  { self.score }", align= ALIGNMENT, font= FONT)
    
    def increase_score(self):
        self.score += 1    
        self.clear()
        self.display_score()

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", align= ALIGNMENT, font= FONT)

from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self) :
        super().__init__()
        self.level = 1
        self.penup()
        self.hideturtle()
        self.goto(-180, 250)
        self.display_level()

    def display_level(self):
        self.clear()
        self.write(f"Level : { self.level }", font=FONT, align="center")

    def level_up(self):
        self.level +=1

    def game_over(self):
        self.goto(0, 0) 
        self.write(f"GAME OVER", font=FONT, align="center")

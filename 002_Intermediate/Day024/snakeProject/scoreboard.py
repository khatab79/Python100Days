from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")

# the path depnds to your machine
PATH ="Day024\snakeProject\data.txt"

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open(PATH,"r") as data:
            self.high_score =  int(data.read())
        self.color("white")
        self.penup()
        self.goto(0, 250)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"High Score: {self.high_score} | Score: {self.score}", align=ALIGNMENT, font=FONT)

    def reset_game(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open(PATH, mode="w") as data:
                data.write(f"{self.score}")
        self.score = 0
        self.update_scoreboard()

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()


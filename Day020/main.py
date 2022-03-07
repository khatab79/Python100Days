from turtle import Screen
import time
from snake import Snake

# Screen setup 
screen = Screen()
screen.setup(width= 600, height= 600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

is_game = True

snake = Snake()

screen.listen()

screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

while is_game:
    screen.update()
    time.sleep(0.1)

    snake.move()

# close screen by clicking x
screen.exitonclick()
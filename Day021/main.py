from turtle import Screen
import time
from snake import Snake
from food import Food
from score import Score

# Screen setup 
screen = Screen()
screen.setup(width= 600, height= 600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

is_game = True
CORDINATE_BORDER_SCREEN = 299

snake = Snake()
food = Food()
score = Score()

screen.listen()

screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

while is_game:
    screen.update()
    time.sleep(0.1)

    snake.move()
    score.display_score()

    # detect food and increase score
    if snake.head.distance(food) < 20:
        food.refrech()
        snake.extend()
        score.increase_score()

    # detect Wall and show GAME OVER
    if snake.head.xcor() > CORDINATE_BORDER_SCREEN or snake.head.xcor() < -1 * CORDINATE_BORDER_SCREEN or snake.head.ycor() > CORDINATE_BORDER_SCREEN or snake.head.ycor() < -1 *  CORDINATE_BORDER_SCREEN:
        score.game_over()
        is_game = False

    # detect tail and show GAME OVER
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10 :
            is_game = False
            score.game_over()

# close screen by clicking x
screen.exitonclick()
from turtle import Screen
from ball import Ball
from paddle import Paddle
from score import Score
import time

SCREEN_HEIGHT = 600
SCREEN_WIDTH = 800

is_game = True

screen = Screen()
screen.setup(height= SCREEN_HEIGHT, width= SCREEN_WIDTH)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)


r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
score = Score()

screen.listen()
screen.onkey(r_paddle.up,"Up")
screen.onkey(r_paddle.down,"Down")
screen.onkey(l_paddle.up,"q")
screen.onkey(l_paddle.down,"a")


while is_game:
    time.sleep(ball.speed_ball)
    screen.update()
    ball.move()
    # detect collision with wall (top and down)
    if ball.ycor() > 285 or ball.ycor() < -285:
        ball.bounce_y()

    # detect collision with paddles
    if (ball.distance(r_paddle) < 50 and ball.xcor() > 330) or (ball.distance(l_paddle) < 50 and ball.xcor() < -330):
        ball.bounce_x()

    # detect missing a ball (right and left) 
    # right
    if ball.xcor()> 380:
        score.increase_score_l()
        ball.reset_position()
       
    # left   
    if ball.xcor()< -380:
        score.increase_score_r()
        ball.reset_position()

screen.exitonclick()
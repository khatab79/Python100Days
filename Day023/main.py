import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

player = Player()
car_manager = CarManager()
score = Scoreboard()

screen.onkey(player.move_up, "Up")
screen.onkey(player.move_down, "Down")

game_is_on = True

while game_is_on:
    score.display_level()
    car_manager.make()
    car_manager.move()

    time.sleep(car_manager.speed_level)
    screen.update()

    # detect collision with cars
    for car in car_manager.cars:      
        if car.distance(player) < 21:
            score.game_over()
            game_is_on = False
        
    # detect finish the race
    if player.ycor() > 280:
        player.replay()
        car_manager.level_up()
        score.level_up()

screen.exitonclick()
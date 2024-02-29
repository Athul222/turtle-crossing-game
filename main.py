import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
car_manager = CarManager()

player = Player() 
scoreboard = Scoreboard()

screen.listen()
screen.onkey(fun=player.movement, key="Up")

game_is_on = True
while game_is_on:
    # Cars are gonna developed every 0.1 times
    time.sleep(0.1) 
    screen.update()
    
    car_manager.create_car()
    car_manager.car_movement()
    
    # Detect collision with player.
    for car in car_manager.all_car:
        # If the distance is less than 20px the they collide
        if car.distance(player) < 20: 
            game_is_on = False
            scoreboard.game_over() 
    
    if player.is_on_finish_line():
        player.go_to_start()
        scoreboard.score()
        car_manager.level_up()
    
screen.exitonclick()

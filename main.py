from turtle import Screen
from my_turtle import MyTurtle
from scoreboard import Scoreboard
from car import CarManager
import time

turtle_player = MyTurtle()
scoreboard = Scoreboard()
car_manager = CarManager()

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.title("Turtle Crossing")
screen.listen()
screen.onkey(turtle_player.move_forward, "w")


game_is_on = True


while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move_cars()
    for car in car_manager.all_cars:
        if car.distance(turtle_player) < 20:
            game_is_on = False
            scoreboard.game_over()

    if turtle_player.is_at_finish_line():
        scoreboard.increase_score()
        turtle_player.go_to_start()
        car_manager.level_up()


screen.exitonclick()










# - Create turtle at bottom of screen
# - Turtle needs ability to travel up

# Create turtle cars at the right of the screen
# - Cars all move left at same speed



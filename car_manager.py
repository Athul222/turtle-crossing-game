from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class CarManager:
    def __init__(self):
        self.all_car = []
        self.car_speed = STARTING_MOVE_DISTANCE
        
    def create_car(self):
        """To decrease the number of cars printing we are gonna use random dicision 
        with the help of random module.
        Now it's going to print new cars every time when random choice is 1."""
        random_choice = random.randint(1, 6)
        if random_choice == 1:
            new_car = Turtle("square")
            new_car.shapesize(stretch_wid= 1, stretch_len= 2)
            new_car.color(random.choice(COLORS))
            new_y = random.randint(-250, 250)
            new_car.penup()
            new_car.goto(350, new_y)
            self.all_car.append(new_car)
            
    def car_movement(self):
        for cars in self.all_car:
            cars.backward(self.car_speed)
            
    def level_up(self):
        # Incrementing the speed of car.
        self.car_speed += MOVE_INCREMENT 
    
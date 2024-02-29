from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("black")
        self.penup()
        self.setheading(90)
        self.go_to_start()
    
    def movement(self):
        self.forward(MOVE_DISTANCE)
    
    def go_to_start(self):
        self.goto(STARTING_POSITION)           
    
    # Detecting whether the turtle have reached the destination point.
    def is_on_finish_line(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False
from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.current_score = 0
        self.update_scoreboard()
    
    def update_scoreboard(self):
        self.clear()
        self.goto(-200, 260)
        self.write(f"Score: {self.current_score}", align="center", font=FONT)
        
    
    def score(self):
        self.current_score += 1
        self.update_scoreboard()
        
    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", align="center", font=FONT)

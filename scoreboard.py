from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        """Inherits the Turtle class' attributes and methods"""
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        """Changes the score based on current points for each player"""
        self.clear()
        self.goto(-150, 200)
        self.write(f"Blue: {self.l_score}", align="center", font=("Courier", 20, "normal"))
        self.goto(150, 200)
        self.write(f"Red: {self.r_score}", align="center", font=("Courier", 20, "normal"))

    def increase_left(self):
        """Raises the attribute l_score by 1 and calls on the update_scoreboard() method"""
        self.l_score += 1
        self.update_scoreboard()

    def increase_right(self):
        """Raises the attribute r_score by 1 and calls on the update_scoreboard() method"""
        self.r_score += 1
        self.update_scoreboard()

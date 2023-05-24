from turtle import Turtle
import random


class Ball(Turtle):
    def __init__(self):
        """Inherits the Turtle class's attributes and methods"""
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.move_speed = 0.1

        # Random starting direction
        self.x_factor = random.choice([-1, 1])
        self.y_factor = random.choice([-1, 1])

    def move(self):
        """Moves in both axes' directions by a random factor of -1 and 1, to change orientation"""
        new_x = self.xcor() + 10 * self.x_factor
        new_y = self.ycor() + 10 * self.y_factor
        self.goto(new_x, new_y)

    def reset_ball(self):
        """Resets the ball to its initial position but going the opposite direction"""
        self.move_speed = 0.1
        self.goto(0, 0)
        self.x_factor *= -1
        self.y_factor *= -1

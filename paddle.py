from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, coord, color, speed=20, orientation="vertical"):
        """Inherits the Turtle class's attributes and methods. Takes in color, speed (paces per tap), and orientation"""
        super().__init__()
        self.shape("square")
        self.color(color)
        self.speed = speed

        # Stretches square shape into a rectangle according to orientation
        if orientation == "horizontal":
            self.shapesize(stretch_wid=1, stretch_len=5)
        else:
            self.shapesize(stretch_wid=5, stretch_len=1)

        self.penup()
        self.goto(coord)

    def go_up(self):
        """Moves up a fixed 20 paces. Event listener on 2-paddles.py and 4-paddles.py"""
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def go_down(self):
        """Moves down a fixed 20 paces if 2 paddles, custom if 4. Event listener on 2-paddles.py and 4-paddles.py"""
        new_y = self.ycor() - self.speed
        self.goto(self.xcor(), new_y)

    def go_left(self):
        """Moves left a fixed 20 paces if 2 paddles, custom if 4. Event listener on 2-paddles.py and 4-paddles.py"""
        new_x = self.xcor() - self.speed
        self.goto(new_x, self.ycor())

    def go_right(self):
        """Moves right a fixed 20 paces if 2 paddles, custom if 4. Event listener on 2-paddles.py and 4-paddles.py"""
        new_x = self.xcor() + self.speed
        self.goto(new_x, self.ycor())

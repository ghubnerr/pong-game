from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

# Creating paddles
right_paddle = Paddle((350,0), "red")
left_paddle = Paddle((-350, 0), "blue")

# Creating ball
ball = Ball()

# Creating scoreboard
scoreboard = Scoreboard()

# Creating paddle controls
screen.listen()
screen.onkey(left_paddle.go_up, "w")
screen.onkey(left_paddle.go_down, "s")
screen.onkey(right_paddle.go_up, "Up")
screen.onkey(right_paddle.go_down, "Down")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detecting collisions
    if ball.ycor() in [-280, 280]:
        ball.y_factor *= -1
    if ball.distance(right_paddle) < 50 and ball.xcor() > 320 or ball.distance(left_paddle) < 50 and ball.xcor() < -320:
        ball.move_speed *= 0.9
        ball.x_factor *= -1

    # Detecting if red player loses
    if ball.xcor() > 340:
        ball.reset_ball()
        scoreboard.increase_right()

    # Detecting if blue player loses
    elif ball.xcor() < -340:
        ball.reset_ball()
        scoreboard.increase_left()


screen.exitonclick()

from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

SPEED = 40

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

# Creating paddles
r_paddle = Paddle((350, 0), "red", speed=SPEED, orientation="vertical")
l_paddle = Paddle((-350, 0), "blue", speed=SPEED, orientation="vertical")
t_paddle = Paddle((0, 280), "blue", speed=SPEED, orientation="horizontal")
b_paddle = Paddle((0, -280), "red", speed=SPEED, orientation="horizontal")

# Creating ball
ball = Ball()

# Creating scoreboard
scoreboard = Scoreboard()

# Creating paddle controls
screen.listen()
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(t_paddle.go_left, "a")
screen.onkey(t_paddle.go_right, "d")
screen.onkey(b_paddle.go_left, "Left")
screen.onkey(b_paddle.go_right, "Right")


game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detecting collisions with a buffer to account for the length of the paddles
    if ball.distance(t_paddle) < 50 and ball.ycor() > 250 or ball.distance(b_paddle) < 50 and ball.ycor() < -250:
        ball.move_speed *= 0.95
        ball.y_factor *= -1
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.move_speed *= 0.95
        ball.x_factor *= -1

    # Detecting if red player loses
    if ball.xcor() > 340 or ball.ycor() < -260:
        ball.reset_ball()
        scoreboard.increase_left()

    # Detecting if blue player loses
    elif ball.xcor() < -340 or ball.ycor() > 260:
        ball.reset_ball()
        scoreboard.increase_right()


screen.exitonclick()

# Pong Game with Python Turtle Module

## The Games

The code uses Object-Oriented Programming and Class Inheritance to create instances of the Turtle class that are treated accordingly to their roles. `ball.py` will have a speed increasing over time depending on the number of bounces that it makes. Its direction is defined by multiplying factors of -1 and 1 to its x, y coordinate assignments, which will reverse depending on the direction of the collision.

`scoreboard.py` is also an instance of a Turtle class, that keeps count of the points by each colored player.

Finally, the instances of `paddle.py` are stretched-out turtle objects created specifically for collision detection with the ball using the *`ball.distance(<object>)`* property with addition to a buffer to ensure that it detects a collision for all the length of the paddle.

### `2-paddles.py`

This version is the original version of the Pong game, where there are only two paddles and the ball has to make it through one of them to score a point.

### `4-paddles.py`

This is a more dynamic version of the game, preferrably played by two people, one controlling the `W, A, S, D` keys for the blue player, and the other controlling the `Up, Down, Left, Right` keys for the red player.
Here, there are no wall bounces, and a point is scored from any sides of the screen. 


## Installation on Local Machine

1. Clone the repository:

   `shell$ git clone https://github.com/ghubnerr/pong-game`

2. Navigate to the project directory:

   `cd pong-game`

3. Run one of the games:
   
   `python 2-paddles.py`, or `python 4-paddles.py`

Alternatively, download the `.zip` file and execute step 3 at the desired directory.

### Requirements:

* Git (for cloning)
* Python 3.x

## License:
This project is licensed under the [MIT License](LICENSE).

## Acknowledgements
Inspirational credit for Dr. Angela Yu and her 100 Days of Code in Python for Udemy.







from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard
import time


# Set-up Screen
width = 800
height = 600
screen = Screen()
screen.setup(width=width, height=height)
screen.colormode(255)
screen.bgcolor("black")
screen.title("Pong game :)")
screen.tracer(0)

# Paddle
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
score_board = ScoreBoard()

# Controls
screen.listen()

# Left paddle
screen.onkey(r_paddle.move_up, "Up")
screen.onkey(r_paddle.move_down, "Down")
screen.onkeypress(fun=r_paddle.move_up, key="Up")
screen.onkeypress(fun=r_paddle.move_down, key="Down")

# Right paddle
screen.onkey(l_paddle.move_up, "z")
screen.onkey(l_paddle.move_down, "s")
screen.onkeypress(fun=l_paddle.move_up, key="z")
screen.onkeypress(fun=l_paddle.move_down, key="s")

# Screen Update
game_is_on = True

while game_is_on:
    time.sleep(ball.ball_speed)
    screen.update()
    ball.move()

    # Detect collision with the top and the bottom
    if ball.ycor() > 290 or ball.ycor() < -280:
        ball.bounce()
        print(ball.ball_speed)
    # Detect collision with the paddle
    if ball.xcor() > 320 or ball.xcor() < -320:
        if ball.distance(r_paddle) < 50 or ball.distance(l_paddle) < 50:
            ball.hit()

    # Detect if the left paddle misses
    if ball.xcor() > 400:
        print("punto para el de la izquierda ")
        score_board.score_left()
        time.sleep(1)
        ball.reset()

    # Detect if the right paddle misses
    elif ball.xcor() < -410:
        print("Punto para el de la derecha")
        score_board.score_right()
        time.sleep(1)
        ball.reset()


# Bottom
screen.exitonclick()

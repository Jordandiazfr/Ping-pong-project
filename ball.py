from turtle import Turtle
import math

width = 800
height = 600
SPEED = 0.1


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.ball_speed = SPEED
        self.x_move = 10
        self.y_move = 10

    def move(self):
        x_now = self.xcor() + self.x_move
        y_now = self.ycor() + self.y_move
        self.goto(x_now, y_now)

    def bounce(self):
        self.y_move *= -1

    def hit(self):
        self.ball_speed *= 0.9
        self.x_move *= -1

    def reset(self):
        self.ball_speed = SPEED
        self.home()
        self.hit()



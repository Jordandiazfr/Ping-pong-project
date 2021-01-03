from turtle import Turtle

STEPS = 30
POSITIONS = [350, -350]


class Paddle(Turtle):
    def __init__(self, position_tuple):
        super().__init__()
        self.shape("square")
        self.setheading(90)
        self.goto(position_tuple)
        self.shapesize(stretch_len=5)
        self.penup()
        self.color("white")

    def move_up(self):
        self.forward(STEPS)

    def move_down(self):
        self.backward(STEPS)


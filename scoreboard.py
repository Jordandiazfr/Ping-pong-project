from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_score()

    def update_score(self):
        self.clear()
        # Left score
        self.goto(-200, 200)
        self.write("%s" % self.r_score, align="center", font=("Courier", 60, "normal"))
        # Right Score
        self.goto(200, 200)
        self.write("%s" % self.l_score, align="center", font=("Courier", 60, "normal"))

    def score_left(self):
        self.l_score += 1
        self.update_score()

    def score_right(self):
        self.r_score += 1
        self.update_score()




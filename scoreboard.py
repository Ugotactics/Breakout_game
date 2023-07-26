from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.pu()
        self.ht()
        self.total_score = 0
        self.scoreboard()

    def scoreboard(self):
        self.clear()
        self.goto(100, 245)
        self.write(self.total_score, align="center", font=("Courier", 40, "normal"))
        self.goto(100, 240)
        self.write('Total score', align="center", font=("Courier", 10, "normal"))

    def increase_red(self):
        self.total_score += 4
        self.scoreboard()

    def increase_blue(self):
        self.total_score += 1
        self.scoreboard()

    def increase_green(self):
        self.total_score += 2
        self.scoreboard()

    def increase_yellow(self):
        self.total_score += 3
        self.scoreboard()


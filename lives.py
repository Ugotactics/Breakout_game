from turtle import Turtle


class Lives(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.pu()
        self.ht()
        self.lives = 5
        self.live()

    def live(self):
        self.clear()
        self.goto(-100, 245)
        self.write(self.lives, align="center", font=("Courier", 40, "normal"))
        self.goto(-100, 240)
        self.write('Total lives', align="center", font=("Courier", 10, "normal"))

    def update_lives(self):
        self.lives -= 1
        self.live()
        return self.lives

from turtle import Turtle


class Bricks(Turtle):

    def __init__(self, color_):
        super().__init__()
        self.shape("square")
        self.color(color_)
        self.pu()
        self.hideturtle()
        self.turtlesize(stretch_len=3.5, stretch_wid=1)

    def set_positioning(self, x, y):
        self.setpos(x, y)
        self.showturtle()

    def brick_disappearing(self):
        self.reset()


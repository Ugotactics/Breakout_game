from turtle import Turtle


class Base_movement(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color('white')
        self.pu()
        self.turtlesize(stretch_len=6, stretch_wid=0.6)
        self.goto(0, -280)

    def move_left(self):
        base_pos = self.xcor() - 30
        self.setx(base_pos)

    def move_right(self):
        base_pos = self.xcor() + 30
        self.setx(base_pos)

from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color('brown')
        self.pu()
        self.turtlesize(stretch_len=0.7, stretch_wid=0.7)
        self.goto(0, -265)
        self.x_move = 10
        self.y_move = 10
        self.speed = 10

    def ball_movement(self):
        set_y = self.ycor() + self.y_move
        set_x = self.xcor() + self.x_move
        self.goto(set_x, set_y)

    def wall_collision(self):
        self.x_move *= -1

    def top_wall_collision(self):
        self.y_move *= -1

    def bounce_off_bat(self):
        self.y_move *= -1
        self.speed *= 0

    def reset_ball(self):
        self.goto(0, 0)
        self.bounce_off_bat()
        self.speed = 0

from turtle import *
from scoreboard import Scoreboard
from bricks import Bricks
from base_movement import Base_movement
from ball import Ball
from lives import Lives

screen = Screen()
screen.setup(width=900, height=600)
screen.title("Breakout game")
screen.bgcolor("black")

##FUNCTION THAT STARTS THE GAME
def start_game():
    base = Base_movement()
    ball = Ball()
    scores = Scoreboard()
    lives = Lives()
    ##LIST OF ALL THE COLOURS FROM ATARI
    brick_color_list = ['blue', 'green', 'yellow', 'red']
    brick_list = []

    ##THIS CREATES THE VARIABLES FOR SETTING THE POSITION
    for i in range(4):
        y = 100 + (20 * i)
        for n in range(0, 12):
            brick = Bricks(brick_color_list[i])
            x = -420 + (74.55 * n)
            brick.set_positioning(x, y)
            brick_list.append(brick)


    screen.listen()

    screen.onkey(base.move_right, "Right")
    screen.onkey(base.move_left, "Left")

    ball_moving = True
    while ball_moving:
        ball.ball_movement()
        screen.tracer(1)
        screen.update()
        ##CHECKS HOW CLOSE THE BALL IS TO THE MOVING BASE AND BOUNCES THE BALL IF IT IS CLOSE ENOUGH
        if (ball.ycor() - base.ycor()) <= 15 and abs((base.xcor() - ball.xcor())) < 60:
            ball.bounce_off_bat()
        ##CHECKS HOW CLOSE THE BALL IS TO THE BAT AND EXECUTES IF THE BALL IS NOT HIT BY THE BAT
        ##IT ALSO ENDS THE GAME IF WE'VE RUN OUT OF LIVES
        if ball.ycor() < -290:
            lives.update_lives()
            if lives.lives == 0:
                screen.reset()
                start_game()
            else:
                ball.reset_ball()
                ##HELPS TO BOUNCE BACK THE BALL WHEN IT HITS THE SIDE WALL
        if ball.xcor() <= -431 or ball.xcor() >= 431:
            ball.wall_collision()
            ##BOUNCES BACK FROM THE TOP WALL
        if ball.ycor() >= 283:
            ball.top_wall_collision()
        for brick in brick_list:
            ##THIS INCREASES THE SCORE LINE
            if (brick.ycor() - ball.ycor()) <= 15 and abs((brick.xcor() - ball.xcor())) <= 30:
                print(brick.ycor())
                if brick.ycor() == 100:
                    scores.increase_blue()
                elif brick.ycor() == 120:
                    scores.increase_green()
                elif brick.ycor() == 140:
                    scores.increase_yellow()
                elif brick.ycor() == 160:
                    scores.increase_red()
                brick.brick_disappearing()
                brick_list.remove(brick)
                ball.bounce_off_bat()
                break


start_game()

screen.exitonclick()

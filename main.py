import random
from turtle import Screen
from paddle import Paddle
from ball import Ball
from score_tracking import Score
import time

screen = Screen()
screen.mode("standard")
player_platform = Paddle((-350, 0))
computer_platform = Paddle((350, 0))
player_platform.seth(0)
computer_platform.seth(180)
ball = Ball()
score = Score()
score.update_score()
ball.ball_apperance()
screen.title("Pong Game")
screen.setup(width=800, height=600)
screen.bgcolor("black")

screen.listen()
# left paddle
screen.onkey(player_platform.up, "Up")
screen.onkey(player_platform.down, "Down")
# right paddle
screen.onkey(computer_platform.up, "w")
screen.onkey(computer_platform.down, "s")
screen.delay(0)

is_on = True

while is_on:
    screen.update()
    screen.tracer(0)
    time.sleep(0.05) #0.015
    if ball.ycor() < 280 or ball.ycor() > -280:
        ball.ball_move()
    if ball.ycor() >= 279:
        ball.setheading(random.randrange(180,325,25))
        ball.start_heading = ball.heading()
        ball.ball_move()
    if ball.ycor() <= -279:
        ball.setheading(random.randrange(25,180,25))
        ball.ball_move()
    if ball.distance(player_platform) < 60 and ball.xcor() < -330 or ball.distance(computer_platform) < 60 and ball.xcor() > 320:
        if ball.distance(player_platform) < 60 and ball.xcor() < -330:
            ball.setheading(abs(180-ball.start_heading))
            ball.ball_move()
        else:
            ball.setheading(random.randrange(135,180,25))
            ball.ball_move()
    if ball.xcor() > 400:
        ball.ball_apperance()
        score.player()
    if ball.xcor() < -400:
        ball.ball_apperance()
        score.computer()

















screen.exitonclick()
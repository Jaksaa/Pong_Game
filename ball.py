from turtle import Turtle
import random


class Ball(Turtle):
    def __init__(self):
        super().__init__()

    def ball_apperance(self):
        self.shape("circle")
        self.penup()
        self.color("blue")
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.setposition(0, 0)
        self.setheading(random.randrange(45, 360, 45))
        self.start_heading = self.heading()
        self.speed(speed=0)

    def ball_move(self):
        self.fd(15)







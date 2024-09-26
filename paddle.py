from turtle import Turtle
import time as t

SPEED = 5
BOUNDARY = 250


class Paddle(Turtle):

    def __init__(self):
        super().__init__()
        self.speed = SPEED
        self.penup()
        self.color("white")
        self.shape("square")
        self.shapesize(stretch_wid=0.4, stretch_len=5)

    def up(self):
        self.forward(self.speed)

    def down(self):
        self.backward(self.speed)

    def paddle_boundary(self):
        if self.ycor() > BOUNDARY:
            self.goto(self.xcor(), self.ycor() - 10)
        elif self.ycor() < -BOUNDARY:
            self.goto(self.xcor(), self.ycor() + 10)

    def enemy_tracking(self, ball):
        if self.ycor() >= ball.ycor():
            self.goto(self.xcor(), self.ycor() - 5)
        elif self.ycor() < ball.ycor():
            self.goto(self.xcor(), self.ycor() + 5)


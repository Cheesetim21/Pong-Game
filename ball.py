from turtle import Turtle
import random as r

SPEED = 7

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.speed = SPEED
        self.penup()
        self.color("white")
        self.shape("circle")
        self.shapesize(stretch_wid=0.8, stretch_len=0.8)
        self.setheading(180)
        self.goto(-5, 0)

    def move(self):
        self.forward(self.speed)

    def hit_paddle(self):
        old_angle = 180 - int(self.heading())
        new_angle = old_angle + r.randint(-20, 20)
        self.setheading(new_angle)
        self.forward(10)

    def hit_wall(self, wall):
        direction = int(self.heading())

        if wall == "top":
            if direction > 90: # moving left
                angle = 180 - direction
                self.setheading(180 + angle)
            elif direction < 90: # moving right
                self.setheading(360 - direction)
            self.goto(self.xcor(), self.ycor() - 26)

        elif wall == "bottom":
            if direction > 270: # moving right
                angle = 360 - direction
                self.setheading(angle)
            elif direction < 270: # moving left
                angle = direction - 180
                self.setheading(180 - angle)
            self.goto(self.xcor(), self.ycor() + 26)

    def reset(self, winner):
        self.goto(0,0)
        if winner == "player":
            self.setheading(0)
        elif winner == "enemy":
            self.setheading(180)



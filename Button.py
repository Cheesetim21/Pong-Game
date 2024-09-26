from turtle import Turtle

class Button(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("square")
        self.shapesize(stretch_wid=4.5, stretch_len=4.5)
        self.fillcolor("")
        self.penup()

    def write_text(self, text):
        if text == "P1":
            self.goto(-100, 0)
        elif text == "P2":
            self.goto(100, 0 )

        self.penup()
        self.goto(self.xcor(), self.ycor() - 20)
        self.write(text, False, "center", ('Courier', 32, 'normal'))










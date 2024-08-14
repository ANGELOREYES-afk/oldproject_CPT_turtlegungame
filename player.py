from turtle import Turtle


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.shape('turtle')
        self.goto(-180, 0)
        self.setheading(0)

    def go_up(self):
        self.setheading(90)
        self.forward(25)

    def go_down(self):
        self.setheading(270)
        self.forward(25)

    def right_1(self):
        self.setheading(0)
        self.forward(25)

    def left_1(self):
        self.setheading(180)
        self.forward(25)

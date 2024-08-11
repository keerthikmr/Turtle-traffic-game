from turtle import Turtle


class Traffic(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_len=2)
        self.color("red")
        self.penup()
        self.setheading(-180)
        self.goto(250, 0)

    def start(self, cars):
        for car in cars:
            car.forward(1)
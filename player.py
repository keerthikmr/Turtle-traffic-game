from turtle import Turtle

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("turtle")
        self.setheading(90)
        self.goto(0, -280)
    

    def up(self):
        self.forward(10)
    

    def down(self):
        self.backward(10)

    
    def release(self):
        pass
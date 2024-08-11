from turtle import Turtle, Screen
import player, traffic
from random import randint
import time 

screen = Screen()
screen.tracer(0)
screen.setup(width=600, height=600)

turtle = player.Player()


game_on = True

cars = []

for i in range(30):
    car = traffic.Traffic()
    cars.append(car)
    coord = (randint(-300,300), randint(-250,280))
    cars[-1].goto(coord)

while game_on:
    screen.update()
    for each in cars:
        y_limit = (each.ycor()+10, each.ycor()-10)
        if each.distance(turtle) < 20 and (turtle.ycor()+10 > y_limit[1] or turtle.ycor()-10 < y_limit[0]):
            screen.update()
            time.sleep(3)

        if each.distance(turtle) < 28 and each.xcor()-20 < 10:
            screen.update()
            time.sleep(3)

        if each.xcor() < -300:
            coord = (randint(300,400), randint(-250,250))
            each.goto(coord)

    screen.onkeypress(turtle.up, "w")
    screen.onkeyrelease(turtle.release, "w")
    
    screen.onkeypress(turtle.down, "s")
    screen.onkeyrelease(turtle.release, "s")
    
    screen.listen()
    
    car.start(cars)
    
screen.mainloop()

from turtle import *

shape("turtle")

bgcolor("black")

speed(0)

for i in range(1,201):
    lt(119)
    fd(i*2)
    if i % 3 == 0:
        color("blue")
    elif i % 3 == 1:
        color("yellow")
    else:
        color("red")

exitonclick()
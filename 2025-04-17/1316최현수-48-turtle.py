from turtle import *

shape("turtle")
color("green")
pensize(3)

for i in range(4):
    fd(100)
    lt(90) # left(90)

color("red")

for i in range(3):
    fd(100)
    lt(120) # left(120)

color("yellow")

fillcolor("yellow")

begin_fill()
circle(50)
end_fill()
exitonclick()
from turtle import *
import random

# up()
# goto(100,100)
# down()
# shape("turtle")
# color("green")
# pensize(3)
# for i in range(5):
#     fd(100)
#     lt(72)

shape("turtle")

cr_lst = ["red", "orange", "yellow", "green", "blue", "navy", "purple"]
cr = random.choice(cr_lst)
color(cr)

print("n각형 만들기")
n = int(input("n을 입력하세요 : "))
d = int(input("한 변 길이 : "))

angle = 360/n

for i in range(n):
    fd(d)
    lt(angle)

exitonclick()
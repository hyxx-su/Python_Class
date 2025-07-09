from turtle import *
import random as r

# x 좌표 범위
x_min = -5; x_max = 5

# y 좌표 범위
y_min = -5; y_max = 5

# 그래프 간격
space = 0.1

# 함수 리스트
func_list = ["x*x", "abs(x)", "0.5*x+1"]
color_list = ["green", "red", "blue", "purple"]

# 사용자 정의 좌표 설정, 거북 속도, 선 굵기
setworldcoordinates(x_min, y_min, x_max, y_max)
speed(4)
pensize(3)

up(); goto(x_min, 0)
down(); goto(x_max, 0)
up(); goto(0, y_min)
down(); goto(0, y_max)

for func in func_list:
    color(r.choice(color_list))
    x = x_min
    y = eval(func)
    up()
    goto(x, y)
    down()

    while x <= x_max:
        x += space
        y = eval(func)
        goto(x, y)

exitonclick()
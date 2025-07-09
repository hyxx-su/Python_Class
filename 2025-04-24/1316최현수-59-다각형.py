from turtle import *

def moving():
    a, b = map(int, input("이동할 좌표(a b) : ").split())
    up()
    goto(a, b)
    down()

def input_data():
    while True:
        x, y = map(int, input("종류(3이상) 한변(5이상) : ").split())
        if x >= 3 and y >= 5:
            return x, y
        else:
            continue

def polygon():
    n, a = input_data()
    for i in range(n):
        fd(a)
        lt(360/n)

# main
print("=== 도형 그리기 ===")
while True:
    moving()
    polygon()
    con = input("계속(Y) / 종료(N) : ").lower()
    if con != "y":
        break

exitonclick()
# 터틀런2

from turtle import *
import random as r

score = 0 # 점수
playing = False # 플래그

tc = Turtle()
tc.shape("turtle")
tc.color("white")
tc.up()
tc.speed(0)

# 악당 객체 생성
tv = Turtle() # 악당 거북(빨간색)
tv.shape("turtle")
tv.color("red")
tv.speed(0)
tv.up()
tv.goto(0,200) # 악당 시작 위치

# 먹이 객체 생성
tf = Turtle()
tf.shape("circle")
tf.color("green")
tf.speed(0)
tf.up()
tf.goto(0, -200) # 먹이 시작 위치

# 움직임 정의
def turn_right():
    tc.setheading(0)

def turn_up():
    tc.setheading(90)

def turn_left():
    tc.setheading(180)

def turn_down():
    tc.setheading(270)

def start():
    global playing
    if playing == False:
        playing = True
        tc.clear()
        play()

# play 함수
def play():
    global score
    global playing

    tc.fd(10) # 주인공 앞으로 이동
    ang = tv.towards(tc.pos()) # 주인공 위치의 각도
    tv.setheading(ang) # 악당이 주인공 쪽을 바라보게
    tv.fd(9) # 악당 앞으로 이동

    if tc.distance(tv) < 12:
        text = (f'score : {score}')
        msg("Game Over", text)
        playing = False
        score = 0

    if tc.distance(tf) < 12: # 주인공과 먹이 거리가 가까우면
        score += 1
        tc.write(score)
        start_x = r.randint(-230, 230)
        start_y = r.randint(-230, 230)
        tf.goto(start_x, start_y) # 먹이를 다른 곳으로 이동
        
    if playing:
        ontimer(play, 100) # 0.1초 후 play 함수 실행 (게임 계속)

def msg(m1, m2):
    hideturtle()
    tc.clear()
    tc.up()
    tc.goto(0, 100)
    tc.down()
    tc.write(m1, False, "center",("",20))
    tc.up()
    tc.goto(0, -100)
    tc.down()
    tc.write(m2, False, "center",("",15))
    tc.up()
    home()

# 게임 준비
def ready():
    setup(500, 500)
    title("Turtle Run")
    bgcolor("orange") # 배경 색
    
# 이벤트에 따른 움직임 설정
def move():
    onkeypress(turn_right, "Right")
    onkeypress(turn_up, "Up")
    onkeypress(turn_left, "Left")
    onkeypress(turn_down, "Down")
    onkeypress(start, "space")
        
# 메인
ready() # 게임 준비
move() # 시작
listen() # 이벤트 감지
msg("Turtle Run", "[Space]")

exitonclick()
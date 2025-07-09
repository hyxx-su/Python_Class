# IMPORT
import random as r

# input
user = int(input("입력(1.가위 2.바위 3.보) :"))

com = r.randint(1, 3)

endprint = "오류"

# 하드 코드
if not user == com:

    if user == 3 and com == 2:
        endprint = "이겼음"

    elif user == 2 and com == 1:
        endprint = "이겼음"

    elif user == 1 and com == 3:
        endprint = "이겼음"

    elif user == 3 and com == 1:
        endprint = "졌음"

    elif user == 2 and com == 3:
        endprint = "졌음"

    elif user == 1 and com == 2:
        endprint = "졌음"

else:
    endprint = "무승부"

# USER 문자 정하기
if user == 1:
    user = "가위"
elif user == 2:
    user = "바위"
elif user == 3:
    user = "보"
else:
    user = "Error"

# COM 문자 정하기
if com == 1:
    com = "가위"
elif com == 2:
    com = "바위"
else:
    com = "보"

# PRINT
print(f'user : {user} com : {com} -> {endprint}')
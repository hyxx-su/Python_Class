# 예외 처리
while True:
    a, b = map(int, input().split())
    try:
        c = a/b
    except ZeroDivisionError:
        print("0으로 못 나눔. 다시 입력해주세요")
    else:
        print(c)
        break


    
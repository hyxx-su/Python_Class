import random as r

list_Q = list(range(1, 7, 1))

Com = r.choices(list_Q, k=2)

User = list(map(int, input("2개 입력(1~6, 중복 허용) : ").split()))

print(f'Com={Com} User={User}')

Com.sort()
User.sort()

v = 0

if Com == User:
    v = 1
elif (Com[0] == User[0]) or (Com[0] == User[1]) or (Com[1] == User[0]) or (Com[1] == User[1]):
    v = 2
else:
    v = 3

print(f'{v}등!')
car = 170

a, b, c = map(int, input().split())

i = 0

if a > b:
    if a > c:
        i = a
    else:
        i = c
elif b > c:
    i = b
else:
    i = c

if car > i:
    print("pass")
else:
    print("crash")
# a = list(map(int, input().split()))
# a.sort()
# print(a[1])

a, b, c = map(int, input().split())

Big = 0
Middle = 0
Small = 0

if a >= b:
    if a >= c:
        Big = a
        if b >= c:
            Middle = b
            Small = c
        else:
            Middle = c
            Small = b
    else:
        Big = c
        Middle = a
        Small = b
elif b >= c:
    Big = b
    if c >= a:
        Middle = c
        Small = a
    else:
        Middle = a
        Small = c
else:
    Big = c
    Middle = b
    Small = a

print(f'2번째 숫자는 {Middle}입니다.')
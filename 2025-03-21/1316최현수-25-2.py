# INPUT
kg = int(input())
value = "아아"

# 조건
a = 210 <= kg and 250 > kg
b = 250 <= kg and 300 > kg
c = 300 <= kg and 375 > kg

# VALUE
A = "\"보통\""
B = "\"상\""
C = "\"특\""
D = "\"판정 불가\""

# IF
if a:
    value = A
elif b:
    value = B
elif c:
    value = C
else:
    value = D

# PRINT
print(value)
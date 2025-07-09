day, gender = map(int, input().split(","))

Today = 2025
year = day//10000
s = "중성"
age = 0

if gender == 1 or gender == 2:
    year += 1900
else:
    year = 2000

age = Today - year

if gender%2 == 0:
    s = "여성"
else:
    s = "남성"

print(f"저는 {age}살의 {s}입니다.")
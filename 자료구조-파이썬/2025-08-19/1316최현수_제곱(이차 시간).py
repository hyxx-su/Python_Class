n = 5
count = 0

for i in range(n):
    for j in range(n):
        count += 1
        print(i, j)

print("총 반복 횟수 : ", count)
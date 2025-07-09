f = open("data_2.txt", "w")

for i in range(1, 11):
    line = f'{i}번째 줄\n'
    f.write(line)

f.close()
print("정상 종료")
f = open("data_2.txt", "a")

for i in range(11, 21):
    content = f'{i}번째 줄\n'
    f.write(content)

f.close()
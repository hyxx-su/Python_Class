i = 0
score = 0

while True:
    int_a = int(input("점수 : "))

    if int_a < 0:
        print(f'최종 점수 : {score}')
        print(f'평균 : {score//i}')
        break
    
    else:
        score += int_a
        i += 1
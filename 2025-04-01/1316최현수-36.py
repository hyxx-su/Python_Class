i = 0
score = 0

while True:
    
    try:
        int_a = int(input("점수 : "))

    except ValueError:

        print("="*28)

        print(f'합계 : {score}점')

        try:
            print(f'평균 : {score//i}점')

        except ZeroDivisionError:
            print('평균 : 0점')

        break
    
    else:
        score += int_a
        i += 1
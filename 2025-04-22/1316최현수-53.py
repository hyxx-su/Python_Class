def lst_create():
    print("*** 리스트 생성")
    lst = list(map(float, input("숫자(공백으로 분리) : ").split()))
    return lst

def lst_append(n):
    print("*** 숫자 추가(문자 입력 사 추가 종료)")
    while True:
        try:
            f = float(input("추가 숫자 : "))
        except ValueError:
            break
        else:
            n.append(f)
    return n

def lst_cal(n):
    a = sum(n)
    b = a/len(n)
    return a, b

def lst_print(a, b):
    print(f'점수 : {a}')
    print(f'합계 : {b[0]} 평균 : {b[1]}')
    return

lst_s = lst_create()
lst_f = lst_append(lst_s)
result = lst_cal(lst_f)

lst_print(lst_f, result)
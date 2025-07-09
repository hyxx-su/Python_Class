import random, time

# 단어 종류
w = ['동백꽃', '기반', '어렵다', '마룻바닥', '속다', '콧노래', '파선', '팽팽하다', '던져두다', '말머리', '레토나크루져', '포텐샤']

n = 0 # pass 개수

input("[낱말연습]\n준비되면 엔터\n")
print("준비 시간 : 3초")
time.sleep(1)
print("준비 시간 : 2초")
time.sleep(1)
print("준비 시간 : 1초")
time.sleep(1)
print("!! START !!")
start = time.time()

while n < 5:
    q = random.choice(w)

    print(f'\n[문제 {n+1}]\n{q}')

    ans = input()
    
    if q == ans:
        n += 1
        print("PASS")
    else:
        print("FAIL")

end = time.time()
re = end - start

print("-"*40)
print(f'걸린 시간 : {re} 초')
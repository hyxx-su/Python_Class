import random, time

# 단어 종류
w = ['cat', 'dog', 'fox', 'monkey', 'mouse', 'panda', 'frog', 'snake', 'wolf']

n = 0 # pass 개수

input("[타자게임] 준비되면 엔터")

start = time.time()

while n < 5:
    q = random.choice(w)

    print(f'\n[문제 {n+1}] \n{q}')

    ans = input()
    
    if q == ans:
        n += 1
        print("pass")
    else:
        print("fail")

end = time.time()
re = end - start

print("-"*40)
print(f'걸린 시간 : {re} 초')
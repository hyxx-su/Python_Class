import math

def func_avg(n): # 평균
    avg = sum(n)/len(n)
    return avg

def func_var(n): # 분산
    vsum = 0
    v = func_avg(n)
    for x in n:
        vsum += (x-v)**2
    return vsum

def func_std(n): # 표준
    var = func_var(n)/len(n)
    std = math.sqrt(var)
    return std

def func_common(n): # 최대공약수, 최소공배수
    gcd = math.gcd(*n)
    lcm = math.lcm(*n)
    return gcd, lcm

# 리스트 입력
lst = list(map(int, input().split()))
print(lst)

# 평균
print(f'평균 : {func_avg(lst)}')

# 분산
print(f'분산 : {func_var(lst)}')

# 표준편차
print(f'표준편차 : {func_std(lst)}')

# 최대공약수, 최소공배수
print(f'최대공약수 : {func_common(lst)[0]} 최소공배수 : {func_common(lst)[1]}')
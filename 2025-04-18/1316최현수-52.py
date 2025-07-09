# 크기 비교 함수 정리
def maxp(a, b):
    if a > b:
        return a
    else:
        return b

# 인자 전달
print(f'큰 수: {maxp(10, 20)}')

# 인자를 표준 입력 받아 전달
a, b = map(int, input().split())
print(f'큰 수: {maxp(a, b)}')
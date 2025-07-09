# # 프로그램 설명
# print("#"*26)
# print("  분초 계산 프로그램")
# print("#"*26)

# # 변수
# second = int(input("초 입력 :"))

# m = second//60
# s = second%60

# # 실행 결과 출력
# print(f'{m}분 {s}초')






# 프로그램 설명
print("#"*26)
print("  분초 계산 프로그램")
print("#"*26)

# 변수
second = int(input("초 입력 :"))

t = second%3600

h = second//3600

m = t//60

print(h)
print(m)
'''
m = (second-((h)*3600))//60
s = second%60

# 실행 결과 출력
print(f'{h}시 {m}분 {s}초')
'''
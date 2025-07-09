# 프로그램 설명
print("#"*26)
print("  원리합계 계산 프로그램")
print("#"*26)

# 변수
money = int(input("예금 금액(원) :")) # 원금
rate = float(input("예금 이율(%) :")) # 이율
d = int(input("예금 기간(년) :")) # 기간

# 원리합계
result = money + ((money * rate) * 0.01 * d)

print("#"*26)

# 실행 결과 출력
print(f'{money}원을 {rate}% 이율로 {d}년간 예치 후 원리합계는 {result:.0f}원')
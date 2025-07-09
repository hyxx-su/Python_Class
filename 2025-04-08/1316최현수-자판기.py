juice = 5
j_money = 800

while juice > 0:

    print("="*28)
    print(f"주스 가격 : {j_money}원")
    print("="*28)
    
    money = int(input("돈을 넣어주세요 : "))

    if money < j_money:
        print("가격을 확인하세요.")
        print(money)
    elif money == j_money:
        print("맛있는 주스 드세요.")
        juice -= 1
    else:
        print(f'맛있는 주스 드시고 잔돈 {money - j_money}원 받아 가세요.')
        juice -= 1

print("주스가 매진되었습니다.")
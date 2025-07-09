# 30-1
input1 = int(input("어디까지 출력할까요? : ")) + 1

for i in range(1,input1):
    print(i)

print("="*28)

# 30-2
input2 = int(input("어디부터 출력할까요? : "))

for i in range(input2, 0, -1):
    print(i)

print("="*28)


# 30-3
input3 = int(input("몇 단? : "))

print(f'=== {input3}단 ===')

for i in range(1,10):
    print(f'{input3} * {i} = {input3*i:2}')

print("="*28)
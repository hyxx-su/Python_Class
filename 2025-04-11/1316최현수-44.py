# 44-1
input_b = int(input("행 수 : ")) + 1
input_c = int(input("열 수 : ")) + 1
print()
for i in range(1,input_b):
    for ii in range(1, input_c):
        print(i * ii, end=" ")
    print()

print("="*28)

 # 44-2
input_b = int(input("행 수 : "))
input_c = int(input("열 수 : "))
range_a = input_b * input_c + 1
print()
for i in range(1,range_a):
    print(f'{i:<2}', end=" ")
    if i % input_c == 0:
        print()
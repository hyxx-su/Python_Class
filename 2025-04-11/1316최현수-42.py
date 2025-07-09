# 42-1
input_a = int(input("자연수 : "))

for i in range(1, input_a + 1):
    if input_a % i == 0:
        print(i)

# 42-2
input_a = int(input("자연수 : "))

for i in range(input_a, 0, -1):
    if input_a % i == 0:
        print(i)
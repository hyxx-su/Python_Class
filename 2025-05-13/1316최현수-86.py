numbers = [2, 4, 6, 8, 10, 1, 3, 5, 7, 9]

numbers[4:5] = [80]
print(numbers)

numbers[2:6] = "hello"
print(numbers)

numbers[2:3] = ['a','b','c'] 
print(numbers)

numbers[8] = ['a', 'b', 'c'] #리스트 전체를 형태 유지하며 대입
print(numbers)

numbers[:] = [1]
print(numbers)
old_list = [1, 2, 'A', False, 3]
result = [i for i in old_list if type(i)==int]
print(result)

result = [i for i in range(1, 10) if i%2 == 0]
print(result)

array = [-1, 0, -4, 24, 5, -10, 2]
result = [i for i in array if i > 0]
print(result)
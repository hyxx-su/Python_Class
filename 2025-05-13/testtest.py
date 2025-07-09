# v_list = []
# n = 5

# for i in range(n):
# 	a_list = []
# 	for ii in range(i+1):
# 		if ii == 0 or ii == i:
# 			a_list.append(1)
# 		else:
# 			a_list.append(v_list[i-1][ii-1]+v_list[i-1][ii])
# 	v_list.append(a_list)
	
# for i in v_list:
# 	print(*i)
	
#############

# pas = [[0 for j in range(6)] for i in range(6)]

# pas[1][1] = 1

# for i in range(2, 6):
# 	for j in range(1, i+1):
# 		pas[i][j] = pas[i-1][j-1] + pas[i-1][j]
		
# for i in range(1, 6):
# 	for j in range(1, i+1):
# 		print(pas[i][j], end=" ")
# 	print()

# a, b = map(int, input().split())

# if a and b:
#     print(True)

# n = int(input())

# while True:
#     if n != 0:
#         print(n)
#         n -= 1
#     else:
#         break

# arr = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# for i in range(3):
# 	print(*arr[i], end=" ")

# 학생들의 점수 [학생1, 학생2, 학생3]
# scores = [
#     [90, 85, 100],
#     [75, 80, 70],
#     [88, 90, 92]
# ]

# for i in range(len(scores))

# 각 학생의 평균을 출력
# 여기에 코드 작성

# import random as r

# alist = []
# count = 0
# a = 0

# while count < 3:
# 	print(a)
# 	a = r.randint(1,10)
	
# 	if not a in alist:
# 		alist.append(a)
# 		count += 1

# n = list(map(int, input().split()))

# print(n,alist)

# a, b = map(int, input().split())
# a = ""
# n = 0

# for i in rnage(a, b+1):
# 	n += i
# 	a += float(i)+"+"
# print(f'{a[len(a)-1]}={n}')

########################################

# a, b = map(int, input().split(","))
# o = ""
# n = 0

# for i in range(a, b+1):
# 	n += i
# 	o += str(i)+"+"
# print(f'{o[:len(o)-1]}={n}')


########################################

# ali = []
# n = input()
# lol = 0

# for i in n:
# 	lol = 0
# 	for ii in n:
# 		if i == ii:
# 			lol += 1
# 	b = f"{i}: {lol}"
# 	if not b in ali:
# 		ali.append(f"{i}: {lol}")

# for i in range(len(ali)):
# 	print(ali[i])

# import sys
# input = sys.stdin.readline()	

# n = input()
# lol = 0
# o = 0
# u = 0
# lista = []

# first = False

# for i in range(len(n)):
#     if lol == 0:
#         if n[i] == "-":
#             u += 1
#             o = int(n[:i])
#             lista.append(o)
#             lol = i + 1
#             first = True
#         elif n[i] == "+":
#             o = int(n[:i])
#             lista.append(o)
#             lol = i + 1
#     else:
#         if n[i] == "-":
#             o = int(n[lol:i])
#             if first:
#                 lista.append(-o)
#             else:
#                 lista.append(o)
#             lol = i + 1
#             u += 1
#             first = True
#         elif n[i] == "+":
#             o = int(n[lol:i])
#             if first:
#                 lista.append(-o)
#             else:
#                 lista.append(o)
#             lol = i + 1

# o = int(n[lol:i+1])

# if first:
#     lista.append(-o)
# else:
#     lista.append(o)

# a = sum(lista)
# print(a)

# def draw_stars(n):
#     if n==1:
#         return ["*"]
    
#     stars = draw_stars(n//3)
#     lists = []

#     for i in stars:
#         lists.append(i*3)
#     for i in stars:
#         lists.append(i+" "*(n//3)+i)
#     for i in stars:
#         lists.append(i*3)
#     return lists

# n = int(input())
# print("\n".join(draw_stars(n)))

# n = list(input())
# for i in n:
# 	print(f'{i}: {n.count(i)}')
# 	while i in n:
# 		n.remove(i)

# s = set(input())
# vowels = set("aeiou")
# print(list(s-vowels))

import random

print(random.randint(1,10000))
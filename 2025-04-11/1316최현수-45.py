# 45-1
a = int(input("행 수 : "))

for i in range(1, a+1):
    for ii in range(i):
        print("*", end=" ")
    print()

# 45-2
a = int(input("행 수 : "))

for i in range(a, 0, -1):
    for ii in range(i):
        print("*", end=" ")
    print()

# 45-3
a = int(input("행 수 : "))

for i in range(1, a+1):
    for ii in range(a-i):
        print(" ", end=" ")
    for iii in range(i):
        print("*", end=" ")
    print()

# 45-4
a = int(input("행 수 : "))

for i in range(a, 0, -1):
    for ii in range(a-i):
        print(" ", end=" ")
    for iii in range(i):
        print("*", end=" ")
    print()

# 45-5
a = int(input("행 수 : "))

for i in range(1, a+1):
    for ii in range(a-i):
        print(" ", end=" ")
    for iii in range(i):
        print("*", end=" ")
    for iiii in range(i-1):
        print("*", end=" ")
    print()

# 45-6
a = int(input("행 수 : "))

for i in range(a, 0, -1):
    for ii in range(a-i):
        print(" ", end=" ")
    for iii in range(i):
        print("*", end=" ")
    for iiii in range(i-1):
        print("*", end=" ")
    print()

# 45-7
a = int(input("행 수 : "))
b = int(a / 2) + 1
for i in range(1, b + 1):
    for ii in range(b-i):
        print(" ", end=" ")
    for iii in range(i):
        print("*", end=" ")
    for iiii in range(i-1):
        print("*", end=" ")
    print()
for i in range(b-1, 0, -1):
    for ii in range(b-i):
        print(" ", end=" ")
    for iii in range(i):
        print("*", end=" ")
    for iiii in range(i-1):
        print("*", end=" ")
    print()
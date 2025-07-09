# 주사위 1
for i in range(1, 7):
    for ii in range(1, 7):
        print(f'({i}, {ii})', end="")
    print()

# 주사위 2
for i in range(1, 7):
    for ii in range(1, 7):
        print(f'({ii}, {i})', end="")
    print()

# 주사위 3
for i in range(1, 7):
    for ii in range(1, 7):
        if i == ii:
            print(f'      ', end="")
        else:
            print(f'({ii}, {i})', end="")
    print()
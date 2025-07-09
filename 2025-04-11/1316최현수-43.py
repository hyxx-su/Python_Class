# 43-1
for i in range(2,10):
    print(f'=== {i}단 ===')

    for ii in range(1,10):
        print(f'{i} * {ii} = {i*ii:2}')
    print()

# 43-2
input_a = int(input("몇 단? : "))

print(f'\n=== {input_a}단 ===\n')

for i in range(1,10):
    print(f'{input_a} * {i} = {input_a*i:2}')
import random as r

start = r.randint(1,10)
end = r.randint(1,10)

while start != end:
    sum = 0

    if start > end:
        start, end = end, start
        
    ranges = range(start, end + 1)

    for i in ranges:
        sum += i

    print(f'{start:<2} ~ {end:<2} => {sum:2}')

    start = r.randint(1,10)
    end = r.randint(1,10)

print(f'{start:<2} ~ {end:<2} => {start:2}')
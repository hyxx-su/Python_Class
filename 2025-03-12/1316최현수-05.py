km = 1.609344

print("^"*26)
print("  속도 변환 (mile -> km)")
print("^"*26)

mile = input("볼 속도(mile) : ")

change = float(mile)*km

print(f'{mile}mile = {(change):.1f}km')
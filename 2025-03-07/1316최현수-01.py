a = 10
b = 20
z = 5

print(a, "+", b, "=", a+b)
print(a, "-", b, "=", a-b)
print(a, "*", b, "=", a*b)
print(a, "/", b, "=", a/b)
print(a, "//", b, "=", a//b)
print(a, "%", b, "=", a%b)
print(a, "**", z, "=", a**z)

# 포멧(형식)
print(f"{a} + {b} = {a+b}")
print(f"{a} - {b} = {a-b}")
print(f"{a} * {b} = {a*b}")
print(f"{a} / {b} = {a/b}")
print(f"{a} // {b} = {a//b}")
print(f"{a} % {b} = {a%b}")
print(f"{a} ** {z} = {a**z}")

c = f'{a}+{b}'
print(c)
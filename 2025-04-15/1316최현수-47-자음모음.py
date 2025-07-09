n = input("영문자열 입력 : ")
print("#"*28)

con_c = 0
vow_c = 0

n = n.replace("a","@")
n = n.replace("e","@")
n = n.replace("i","@")
n = n.replace("o","@")
n = n.replace("u","@")

for i in n:
    if i.isspace():
        pass
    elif "@" in i:
        vow_c += 1
    else:
        con_c += 1

print(f'모음 : {vow_c} 자음 : {con_c}')
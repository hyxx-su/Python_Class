import random as r

def genPass():
    chr = "abcdefghijklmnopqrstuvwxyz0123456789"
    passwd = ""
    for i in range(8):
        v = r.choice(chr)
        passwd += v
    return passwd

for i in range(3):
    result = genPass()
    print(f'암호 {i+1} : \033[31m {result} \033[0m')
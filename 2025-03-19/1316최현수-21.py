# cm/kg 입력
height = float(input("키(cm) : "))
weight = float(input("체중(kg) : "))

# 조건
CM = (height>=130 and height<190) # 130 <= height < 190
KG = (weight>=25 and weight<100) # 25 <= weight < 100

# PRINT
print("#"*16)

# IF
if CM and KG:
    print("이용 가능")
else:
    print("이용 불가능")
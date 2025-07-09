# 딕셔너리를 생성
stu1 = {'학반':105, '번호':20, '이름':'홍길동'}

# PRINT
print(stu1)

# 연락처를 딕셔너리에 추가
stu1['연락처'] = '010-1111-2222'

# PRINT
print(stu1)

# 동아리를 딕셔너리에 추가
stu1['동아리'] = '파이썬 동아리'

# PRINT
print(stu1)

# 딕셔너리에서 연락처 삭제
del stu1['연락처']

# PRINT
print(stu1)

# 딕셔너리에 있는 동아리 이름을 CNS 변경
stu1['동아리'] = 'CNS'

# PRINT
print(stu1)


#######################################

print(stu1['학반'])
print(stu1['번호'])
print(stu1['이름'])

print(stu1.get('이름'))

# print(stu1.get('주소')) # 오류
# print(stu1('주소')) # 에러

print(stu1.keys())
print(list(stu1.keys()))

print(stu1.values())
print(list(stu1.values()))

print('이름' in stu1)
print('주소' in stu1)
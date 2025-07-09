# LIST 생성
name = ['홍길동', '일지매']

# PRINT
print(f'현재 프로그래밍 수강 신청자는 {name}입니다.')

# LIST 추가
newname = input("추가할 학생 이름:") # 리스트에 추가할 이름 입력
name.append(newname) # 입력한 것을 리스트에 추가

# PRINT
print(f'{newname} 학생이 신청 완료되었습니다.')
print(f'현재 이 과목의 최종 신청자는 {name}입니다.')

# LIST 삭제
delname = input("철회할 학생 이름:") # 리스트에서 삭제할 이름 입력
name.remove(delname) # 입력한 것을 리스트에서 삭제

# PRINT
print(f'{newname} 학생의 수강 철회가 완료되었습니다.')
print(f'현재 이 과목의 최종 신청자는 {name}입니다.')

# LIST 변경
aname = input("변경 전 이름:") # 리스트에서 변경할 이름 입력
bname = input("변경 후 이름:") # 바뀐 이름 입력
where = name.index(aname) # 입력한 이름 위치를 저장
del name[where] # 저장한 위치에 있는 값을 삭제
# name.remove(aname) 위치를 모를 때 바꿀 수 있음
name.insert(where, bname) # 리스트에 바뀐 이름을 입력한 위치에 추가

# PRINT
print(f'요청하신 대로 {aname}을(를) 이지매(으)로 변경하였습니다.') 
print(f'현재 이 과목의 최종 신청자는 {name}입니다.')
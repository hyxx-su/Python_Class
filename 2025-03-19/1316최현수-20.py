# 로그인이 될 ID/PW 지정
id = "dgsw"
pw = "high"

# 로그인이 되지 않음
login = False

# ID/PW 입력
loadid = input("아이디를 입력하세요.\n")
loadpw = input("비밀번호를 입력하세요.\n")

# 로그인 ID, PW 확인
if loadid == id and loadpw == pw:
    login = True
else:
    login = False
    
# 로그인 메시지 출력
if login:
    print("로그인되었습니다.")
else:
    print("로그인에 실패했습니다.")
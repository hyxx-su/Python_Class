# 라이브러리 설치
# pip install pillow

# 이미지 모듈 호출
from PIL import Image

# 이미지 열기
img = Image.open("sample.jpg") # 같은 폴더에 있는 이미지
img.show() # 기본 이미지 뷰어로 열기

# 이미지 정보 확인
print("이미지 크기 : ", img.size) # 크기는 튜플형(가로, 세로)
print("이미지 형식 : ", img.format) # JPEG, PNG 등
print("이미지 모드 : ", img.mode) # RGB, L(흑백) 등

# 이미지 크기 조절
resized = img.resize((200,200))
resized.show()

# 이미지 회전
rotated = img.rotate(90)
rotated.show()

# 이미지 흑백 변환
gray = img.convert("L")
gray.show()

# 이미지 저장
gray.save("gray_sample.jpg")
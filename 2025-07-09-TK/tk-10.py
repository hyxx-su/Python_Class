from tkinter import * # tkinter 라이브러리에서 모든 모듈, 함수 가져오기

root = Tk() # Tk 클래스로 root 생성
root.geometry("300x200") # 창 크기 지정

# 위쪽에 가로로 확장한 버튼
top_btn = Button(root, text = "Top")
top_btn.pack(side = "top", fill = "x") # 위쪽에 배치하고 가로로 확장

# 아래쪽에 가로로 확장한 버튼
bottom_btn = Button(root, text = "Bottom")
bottom_btn.pack(side = "bottom", fill = "x") # 위쪽에 배치하고 가로로 확장

# 왼쪽에 가로로 확장한 버튼
left_btn = Button(root, text = "Left")
left_btn.pack(side = "left", fill = "x") # 위쪽에 배치하고 가로로 확장

# 오른쪽에 가로로 확장한 버튼
right_btn = Button(root, text = "Right")
right_btn.pack(side = "right", fill = "x") # 위쪽에 배치하고 가로로 확장

# 중앙에 가로로 확장한 버튼
center_label = Label(root, text = "Center Area", bg = "lightgray") # 중앙 영역을 나타내는 레이블
center_label.pack(expand = True, fill = "both") # 위쪽에 배치

root.mainloop() # root 닫을 때까지 이벤트 루프에서 대기1
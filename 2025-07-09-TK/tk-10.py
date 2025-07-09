from tkinter import * # tkinter 라이브러리에서 모든 모듈, 함수 가져오기

root = Tk() # Tk 클래스로 root 생성
root.geometry("300x200") # 창 크기 지정

# 위쪽에 가로로 확장한 버튼
top_btn = Button(root, text = "Top")
top_btn.pack(side = "top", fill = "x") # 위쪽에 배치하고 가로로 확장



root.mainloop() # root 닫을 때까지 이벤트 루프에서 대기1
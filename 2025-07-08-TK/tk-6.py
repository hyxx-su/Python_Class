from tkinter import * # tkinter 라이브러리에서 모든 모듈, 함수 가져오기

window = Tk() # Tk 클래스로 루트 윈도 생성

lbl1 = Label(window, text = "레이블입니다")
btn1 = Button(window, text = "One")
btn2 = Button(window, text = "Two")

lbl1.pack()
btn1.pack(side = LEFT, padx = 10) # 외부 여백 주어 가로로 배치. 안쓰면 0
btn2.pack(side = LEFT, padx = 10) # side = RIGHT 로 수정해서 결과 보기
# btn1["text"] = "One" # btn1.config(text = "One") # 버튼 내용 수정
# btn2["text"] = "Two"

window.mainloop() # 윈도 닫을 때까지 이벤트 루프에서 대기
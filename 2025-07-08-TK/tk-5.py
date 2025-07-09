from tkinter import * # tkinter 라이브러리에서 모든 모듈, 함수 가져오기

window = Tk() # Tk 클래스로 루트 윈도 생성

lbl1 = Label(window, text = "레이블입니다")
btn1 = Button(window, text = "1번 버튼")
btn2 = Button(window, text = "2번 버튼")

lbl1.pack()
btn1.pack()
btn2.pack()

window.mainloop() # 윈도 닫을 때까지 이벤트 루프에서 대기
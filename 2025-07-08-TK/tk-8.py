from tkinter import * # tkinter 라이브러리에서 모든 모듈, 함수 가져오기

def print_1():
    lbl1["text"] = "첫 번째 버튼 클릭"

def print_2():
    btn2["text"] = "두 번째 버튼 클릭"

window = Tk() # Tk 클래스로 루트 윈도 생성

lbl1 = Label(window, text = "결과 출력 레이블")
btn1 = Button(window, text = "One", command = print_1)
btn2 = Button(window, text = "Two", command = print_2)

lbl1.pack()
btn1.pack()
btn2.pack()

window.mainloop() # 윈도 닫을 때까지 이벤트 루프에서 대기
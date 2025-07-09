from tkinter import * # tkinter 라이브러리에서 모든 모듈, 함수 가져오기

def callback():
    button["text"] = "버튼이 클릭됨"

window = Tk() # Tk 클래스로 루트 윈도 생성

button = Button(window, text = "클릭", commend = callback)
button.pack(side = LEFT)

window.mainloop() # 윈도 닫을 때까지 이벤트 루프에서 대기
from tkinter import * # tkinter 라이브러리에서 모든 모듈, 함수 가져오기

def add():
    a = int(ent1.get()) # ent1 위젯에서 입력된 문자열을 정수로 변환
    b = int(ent2.get()) # ent2 위젯에서 입력된 문자열을 정수로 변환
    lbl1["text"] = a + b # lbl1 위젯의 텍스트를 a와 b의 합으로 설정

window = Tk() # Tk 클래스로 루트 윈도 생성

ent1 = Entry(window) # Entry 위젯 생성
ent2 = Entry(window) # Entry 위젯 생성
lbl1 = Label(window, text = "결과")
btn1 = Button(window, text = "더하기", command = add) # 버튼 위젯 생성, 클릭 시 add 함수 호출

ent1.pack()
ent2.pack()
lbl1.pack()
btn1.pack()

window.mainloop() # 윈도 닫을 때까지 이벤트 루프에서 대기
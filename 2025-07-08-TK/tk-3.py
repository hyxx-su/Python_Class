from tkinter import * # tkinter 라이브러리에서 모든 모듈, 함수 가져오기

window = Tk() # Tk 클래스로 루트 윈도 생성

label = Label(window, text = "레이블입니다!")
# 루트 윈도에 레이블 위젯 생성
label.pack() # 레이블 배치

window.mainloop() # 윈도 닫을 때까지 이벤트 루프에서 대기
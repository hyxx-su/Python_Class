from tkinter import * # tkinter 라이브러리에서 모든 모듈, 함수 가져오기

window = Tk() # Tk 클래스로 루트 윈도 생성

lbl1 = Label(window, text = "이것은 레이블입니다.")
lbl2 = Label(window, text = "문자를", font = ("궁서체", 20, "bold"))
lbl3 = Label(window, text = "출력하는", bg = "yellow", fg = "red", anchor = "w")
lbl4 = Label(window, text = "위젯입니다.", width = 20, height = 3, bg = "skyblue", anchor = "se")

lbl1.pack()
lbl2.pack()
lbl3.pack()
lbl4.pack()

window.mainloop() # 윈도 닫을 때까지 이벤트 루프에서 대기
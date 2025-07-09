from tkinter import * # tkinter 라이브러리에서 모든 모듈, 함수 가져오기

window = Tk() # Tk 클래스로 루트 윈도 생성

window.title("창 제목")
window.geometry("640x400+100+100") # 창 크기, 메인화면 시작 좌표
window.resizable(1, 0)  # 가로는 조절 가능, 세로는 조절 불가

window.mainloop() # 윈도 닫을 때까지 이벤트 루프에서 대기
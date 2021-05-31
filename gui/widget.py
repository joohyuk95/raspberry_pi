from tkinter import *

window = Tk() # 위젯 창을 만들어주는 클래스

# 화면을 구성하고 처리하는 코드
window.title("윈도우 창 연습")
window.geometry("400x100")
window.resizable(width=False, height=False)

# label
label1 = Label(window, text="fsfsdf")
label2 = Label(window, text="열심히", font=("궁서체", 30), fg='blue')
label3 = Label(window, text="공부 중입니다.", bg = '#ffffff', width=20, height=5, anchor=SE)

label2.pack()
label1.pack()
label3.pack()

window.mainloop() # 실행, 나가기 버튼을 누르기전에는 무한루프
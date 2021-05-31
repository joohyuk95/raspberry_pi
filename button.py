from tkinter import *

window = Tk()

window.title("윈도우 버튼 연습")

button1 = Button(window, text="창 닫기", font=("맑은고딕", 30), command=quit)

button1.pack()

window.mainloop()
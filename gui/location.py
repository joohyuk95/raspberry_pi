from tkinter import *
window = Tk()
window.title("배치 연습")
window.geometry("400x500")

button1 = Button(window, text="1번")
button2 = Button(window, text="2번")
button3 = Button(window, text="3번")
button4 = Button(window, text="4번")

button1.place(x=20, y=20, width=360,height=140)
button2.place(x=20, y=180, width=170,height=140)
button3.place(x=210, y=180, width=170,height=140)
button4.place(x=20, y=340, width=360,height=140)


window.mainloop()
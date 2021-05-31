from tkinter import *
import RPi.GPIO as GPIO
import time
import threading
from PIL import Image, ImageTk

window = Tk()
window.title("에프엔디")
window.geometry("400x400")

GPIO.setmode(GPIO.BOARD)
a=37; b=35; c=33; d=31; e=29; f=23; g=21; h=19
pinData = [a, b, c, d, e, f, g, h]
pinFND = [32, 24, 22, 18, 16, 12]

GPIO.setup(pinData, GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(pinFND, GPIO.OUT, initial=GPIO.HIGH)

Data = [0b00111111, 0b00000110, 0b01011011, 0b01001111,
        0b01100110, 0b01101101, 0b01111101, 0b00100111,
        0b01111111, 0b01101111, 0b01110111, 0b01111100,
        0b01011000, 0b01011110, 0b01111001, 0b01110001]

data = "000000"

def fndDataOut(data):
    for i in range(8):
        GPIO.output(pinData[i], (data >> i) & 0x1)
        
def FND_disp(a):
    global data
    data = entry_FND.get()
    
def fnd_display(num):
    length = len(num)
    if length > 6:
        length = 6
        
    for i in range(length):
        GPIO.output(pinFND[i], GPIO.LOW)
        fndDataOut(Data[int(num[i])])
        time.sleep(0.001)
        GPIO.output(pinFND[i], GPIO.HIGH)
        
def thread1_func():
    while True:
        fnd_display(data)
        
        if thread_stop == 1:
            break
try:
    t1 = threading.Thread(target=thread1_func)
    t1.start()
    thread_stop = 0

    img_FND = Image.open("image_file/FND.png")
    disp_FND = ImageTk.PhotoImage(img_FND)
    label_FND = Label(window, image=disp_FND)
    label_FND.pack()
    
    label_help = Label(window, text="Input Data\n(0~999999)",
                        font=("time", 14, "bold"), bg="#004483", fg="white")
    label_help.pack()
    
    entry_FND = Entry(window, text="Input FND data", width=6,
                      font=("time", 14, "bold"))
    entry_FND.pack()
    entry_FND.bind("<Return>", FND_disp)
    
    window.mainloop()
    
    t1.join()
    
except KeyboardInterrupt:
    thread_stop = 1
    pass

finally:
    thread_stop = 1
    GPIO.cleanup()
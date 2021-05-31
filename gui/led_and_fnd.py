import RPi.GPIO as GPIO
import time
import threading
from tkinter import *
from PIL import Image, ImageTk

##################################### 그래픽 설정 ##########################################

window = Tk()
window.title("이것저것")
window.geometry("310x420")

#####################################  핀 설정   ##########################################

GPIO.setmode(GPIO.BOARD)
a=37; b=35; c=33; d=31; e=29; f=23; g=21; h=19
pinData = [a, b, c, d, e, f, g, h]
pinFND = [32, 24, 22, 18, 16, 12]
LED = [11, 13]

GPIO.setup(pinData, GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(pinFND, GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(LED, GPIO.OUT, initial=GPIO.LOW)


Data = [0b00111111, 0b00000110, 0b01011011, 0b01001111,
        0b01100110, 0b01101101, 0b01111101, 0b00100111,
        0b01111111, 0b01101111, 0b01110111, 0b01111100,
        0b01011000, 0b01011110, 0b01111001, 0b01110001]

#####################################  전역 변수  ##########################################

LED_STATE = [0, 0]
data = "000000"
blink_time = [0.1, 0.3]


##################################### 사용자 함수 ##########################################

################## LED 관련 ##################
def LED0_CH():
    if LED_STATE[0] == 0:
        label_led0.config(image = disp_led0)
        button1["text"] = "LED ON"
        LED_STATE[0] = 1
    else:
        label_led0.config(image = disp_led1)
        button1["text"] = "LED OFF"
        LED_STATE[0] = 0
        
def LED1_CH():
    if LED_STATE[1] == 0:
        label_led1.config(image = disp_led0)
        button2["text"] = "LED ON"
        LED_STATE[1] = 1
    else:
        label_led1.config(image = disp_led1)
        button2["text"] = "LED OFF"
        LED_STATE[1] = 0
                
def time_change0(a):
    blink_time[0] = float(entry_led0.get())

def time_change1(a):
    blink_time[1] = float(entry_led1.get())


###################### FND 관련 ####################
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


#####################################  스레드 함수  ##########################################
        
def thread1_func():
    while True:
        if thread1_stop == 1:
            break
        fnd_display(data)

def LED0_ON():
   while True:
        if thread2_stop == 1:
            GPIO.output(LED[0], GPIO.LOW)
            break
        if LED_STATE[0] == 1:
            GPIO.output(LED[0], GPIO.HIGH)
            time.sleep(blink_time[0])
            GPIO.output(LED[0], GPIO.LOW)
            time.sleep(blink_time[0])
        else:
            GPIO.output(LED[0], GPIO.LOW)
            
def LED1_ON():
   while True:
        if thread3_stop == 1:
            GPIO.output(LED[1], GPIO.LOW)
            break
        if LED_STATE[1] == 1:
            GPIO.output(LED[1], GPIO.HIGH)
            time.sleep(blink_time[1])
            GPIO.output(LED[1], GPIO.LOW)
            time.sleep(blink_time[1])
        else:
            GPIO.output(LED[1], GPIO.LOW)
            
#####################################  메인 함수  ##########################################
try:    
    img_FND = Image.open("image_file/FND.png")
    img_led0 = Image.open("image_file/LED_ON.png")
    img_led1 = Image.open("image_file/LED_OFF.png")
    img_FND = img_FND.resize((250, 70))
    img_led0 = img_led0.resize((50, 80))
    img_led1 = img_led1.resize((50, 80))
    
    disp_FND = ImageTk.PhotoImage(img_FND)
    disp_led0 = ImageTk.PhotoImage(img_led0)
    disp_led1 = ImageTk.PhotoImage(img_led1)
    
    label_FND = Label(window, image=disp_FND)
    label_led0 = Label(window, image=disp_led1)
    label_led1 = Label(window, image=disp_led1)
    
    
    entry_FND = Entry(window, text="Input FND data", width=6,
                      font=("time", 12, "bold"), justify="center")
    entry_led0 = Entry(window, width=6, font=("time", 12, "bold"), justify="center")
    entry_led1 = Entry(window, width=6, font=("time", 12, "bold"), justify="center")
    
    button1 = Button(window, text="LED 1", font=("time", 12, "bold"),command=LED0_CH)
    button2 = Button(window, text="LED 2", font=("time", 12, "bold"),command=LED1_CH)
    
    label_FND.place(x=30, y=30)
    label_led0.place(x=80, y=180)
    label_led1.place(x=180, y=180)
    entry_FND.place(x=30, y=120, width=250, height=30)
    entry_led0.place(x=60, y=360, width=90, height=30)
    entry_led1.place(x=160, y=360, width=90, height=30)
    button1.place(x=60, y=280, width=90, height=60)
    button2.place(x=160, y=280, width=90, height=60)
    
    thread1_stop = 0
    thread2_stop = 0
    thread3_stop = 0
    t1 = threading.Thread(target=thread1_func)
    t1.start()
    t2 = threading.Thread(target=LED0_ON)
    t2.start()
    t3 = threading.Thread(target=LED1_ON)
    t3.start()
    
    entry_FND.bind("<Return>", FND_disp)
    entry_led0.bind("<Return>", time_change0)
    entry_led1.bind("<Return>", time_change1)
    
    window.mainloop()
    
    t2.join()
    t3.join()
    t1.join()
    
except KeyboardInterrupt:
    pass

finally:
    thread1_stop = 1
    thread2_stop = 1
    thread3_stop = 1
    GPIO.output(pinFND, GPIO.HIGH)
    GPIO.output(LED, GPIO.LOW)
    GPIO.cleanup()
import threading
import time
import RPi.GPIO as GPIO
from tkinter import *

GPIO.setmode(GPIO.BOARD)
LED = [11, 13]
GPIO.setup(LED, GPIO.OUT, initial=GPIO.LOW)
LED_STATE = [0, 0]

def LED0_func():
    while True:
        if thread_end == 1:
            GPIO.output(LED[0], GPIO.LOW)
            break
        if LED_STATE[0] == 1:
            GPIO.output(LED[0], GPIO.HIGH)
            time.sleep(0.3)
            GPIO.output(LED[0], GPIO.LOW)
            time.sleep(0.3)
        else:
            GPIO.output(LED[0], GPIO.LOW)
        
def LED1_func():
    while True:
        if thread_end == 1:
            GPIO.output(LED[1], GPIO.LOW)
            break
        if LED_STATE[1] == 1:
            GPIO.output(LED[1], GPIO.HIGH)
            time.sleep(0.5)
            GPIO.output(LED[1], GPIO.LOW)
            time.sleep(0.5)
        else:
            GPIO.output(LED[1], GPIO.LOW)
        
def LED0_CH():
    if LED_STATE[0] == 0:
        LED_STATE[0] = 1
    else:
        LED_STATE[0] = 0
        
def LED1_CH():
    if LED_STATE[1] == 0:
        LED_STATE[1] = 1
    else:
        LED_STATE[1] = 0    

window = Tk()
window.geometry("200x400")

try:
    thread_end = 0
    t1 = threading.Thread(target = LED0_func)
    t2 = threading.Thread(target = LED1_func)
    
    t1.start()
    t2.start()
    
    button1 = Button(window, text="LED 1번", command=LED0_CH)
    button2 = Button(window, text="LED 2번", command=LED1_CH)
    button1.place(x=20, y=20, width=160, height=170)
    button2.place(x=20, y=210, width=160, height=170)

    window.mainloop()
    
    t1.join()
    t2.join()
    
except KeyboardInterrupt:
    pass

finally:
    GPIO.cleanup()
    thread_end = 1
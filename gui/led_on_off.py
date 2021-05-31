from tkinter import *
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
LED = [11, 13]
GPIO.setup(LED, GPIO.OUT, initial=GPIO.LOW)
LED_STATE = [0, 0]

window = Tk()
window.title("LED ON-OFF")
window.geometry("200x400")

def LED0_ON():
    if LED_STATE[0] == 0:
        GPIO.output(LED[0], GPIO.HIGH)
        button1["text"] = "LED ON"
        LED_STATE[0] = 1
    else:
        GPIO.output(LED[0], GPIO.LOW)
        button1["text"] = "LED OFF"
        LED_STATE[0] = 0

def LED1_ON():
    if LED_STATE[1] == 0:
        GPIO.output(LED[1], GPIO.HIGH)
        button2["text"] = "LED ON"
        LED_STATE[1] = 1
    else:
        GPIO.output(LED[1], GPIO.LOW)
        button2["text"] = "LED OFF"
        LED_STATE[1] = 0        

try:
    button1 = Button(window, text="LED 1번", command=LED0_ON)
    button2 = Button(window, text="LED 2번", command=LED1_ON)
    button1.place(x=20, y=20, width=160, height=170)
    button2.place(x=20, y=210, width=160, height=170)

    window.mainloop()

except KeyboardInterrupt:
    pass
finally:
    GPIO.cleanup()
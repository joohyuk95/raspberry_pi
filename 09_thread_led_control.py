import threading
import time
import RPi.GPIO as GPIO


GPIO.setmode(GPIO.BOARD)

LED = [11, 13] 
GPIO.setup(LED, GPIO.OUT, initial = GPIO.LOW)

def LED0_func():
    while True:
        GPIO.output(LED[0], GPIO.HIGH)
        time.sleep(0.3)
        GPIO.output(LED[0], GPIO.LOW)
        time.sleep(0.3)
        
def LED1_func():
    while True:
        GPIO.output(LED[1], GPIO.HIGH)
        time.sleep(0.5)
        GPIO.output(LED[1], GPIO.LOW)
        time.sleep(0.5)

try:
    t1 = threading.Thread(target=LED0_func)
    t2 = threading.Thread(target=LED1_func)

    t1.start()
    t2.start()
    
    while True:
        pass
    
except KeyboardInterrupt:
    pass

finally:
    GPIO.cleanup()    

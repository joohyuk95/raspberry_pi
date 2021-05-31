import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

LED = [19, 21, 23, 29, 31, 33, 35, 37]

for i in range(len(LED)):
    GPIO.setup(LED[i], GPIO.OUT, initial=GPIO.LOW)

try:
    while True:
        for i in range(len(LED)):
            GPIO.output(LED[i], GPIO.HIGH)
        
        time.sleep(0.5)
        
        for i in range(len(LED)):
            GPIO.output(LED[i], GPIO.LOW)

        time.sleep(0.5)

finally:
    GPIO.cleanup()
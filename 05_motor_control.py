import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

P = 15
N = 13

dc = [0, 10, 20, 30, 40, 50, 60, 100]

GPIO.setup(P, GPIO.OUT, initial=HIGH)
GPIO.setup(N, GPIO.IN, initial=LOW)
GPIO.setup(11, GPIO.OUT)

EN = GPIO.PWM(11, 100)
EN.start(0)

try:
    while True:
        for val in dc:
            EN.ChangeDutyCycle(val)
            time.sleep(0.5)

except KeyboardInterrupt:
    EN.stop()
    
finally:
    GPIO.cleanup()
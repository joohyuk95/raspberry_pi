import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

LED = 11
GPIO.setup(LED, GPIO.OUT, initial=GPIO.LOW)

while True:
    GPIO.output(LED, GPIO.HIGH)
    time.sleep(0.5)
    GPIO.output(LED, GPIO.LOW)
    time.sleep(0.5)
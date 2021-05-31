import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

LEDs = [19, 21, 23, 29, 31, 33, 35, 37]


GPIO.setup(LEDs, GPIO.OUT, initial=GPIO.LOW)

GPIO.output(LEDs, GPIO.LOW)
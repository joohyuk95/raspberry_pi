import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

LEDs = [19, 21, 23, 29, 31, 33, 35, 37]


GPIO.setup(LEDs, GPIO.OUT, initial=GPIO.LOW)

try:
    while True:
        GPIO.output(LEDs, GPIO.HIGH)

except KeyboardInterrupt:
    print("키보드 예외")
finally:
    print("cleanup")
    GPIO.cleanup()
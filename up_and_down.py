import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

LEDs = [19, 21, 23, 29, 31, 33, 35, 37]


GPIO.setup(LEDs, GPIO.OUT, initial=GPIO.LOW)

try:
    while True:
        for LED in LEDs:
            GPIO.output(LED, GPIO.HIGH)
            time.sleep(0.05)
            GPIO.output(LED, GPIO.LOW)
        
        for i in range(len(LEDs)-2, 0, -1):
            GPIO.output(LEDs[i], GPIO.HIGH)
            time.sleep(0.05)
        GPIO.output(LEDs[i], GPIO.LOW)

finally:
    print("cleanup")
    GPIO.cleanup()
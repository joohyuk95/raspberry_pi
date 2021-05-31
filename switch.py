import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

switch = 5
led = 11

GPIO.setup(led, GPIO.OUT, initial = GPIO.LOW)
GPIO.setup(switch, GPIO.IN)


try:
    ison = 0
    while True:
        key_in = GPIO.input(switch)
        
        if ison == 0 and key_in == GPIO.HIGH:  #button on (풀다운 저항)
            GPIO.output(led, GPIO.HIGH)  # led off
            ison = 1
        elif ison == 1 and key_in == GPIO.HIGH:
            GPIO.output(led, GPIO.LOW)
            ison = 0
            
    
finally:
    GPIO.cleanup()
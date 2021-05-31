import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

LED = [11, 13] 
SW = [16, 18]

GPIO.setup(LED, GPIO.OUT, initial = GPIO.LOW)
GPIO.setup(SW, GPIO.IN)

def LED_cntl(channel):
    global LED_state
    
    if channel == SW[0]:
        if LED_state[0] == False:
            GPIO.output(LED[0], GPIO.HIGH)
            LED_state[0] = True
        else:
            GPIO.output(LED[0], GPIO.LOW)
            LED_state[0] = False
    else:
        if LED_state[1] == False:
            GPIO.output(LED[1], GPIO.HIGH)
            LED_state[1] = True
        else:
            GPIO.output(LED[1], GPIO.LOW)
            LED_state[1] = False

try:
    LED_state = [False, False]
    GPIO.add_event_detect(SW[0], GPIO.RISING, callback=LED_cntl)
    GPIO.add_event_detect(SW[1], GPIO.RISING, callback=LED_cntl)
    
    while True:
        pass
    
except KeyboardInterrupt:
    pass

finally:
    GPIO.cleanup()
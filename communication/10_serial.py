from serial import Serial
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
led = 11

GPIO.setup(led, GPIO.OUT, initial=GPIO.LOW)

ser = Serial('/dev/ttyACM1', 115200)

while True:
    if ser.readable():
        res = ser.readline()
        message = res.decode()[:len(res)-2]

        if message == "ON":
            GPIO.output(led, GPIO.HIGH)
        elif message == "OFF":
            GPIO.output(led, GPIO.LOW)

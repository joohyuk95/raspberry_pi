import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
a=37; b=35; c=33; d=31; e=29; f=23; g=21; h=19
pinData = [a, b, c, d, e, f, g, h]
pinFND = [32, 24, 22, 18, 16, 12]

GPIO.setup(pinData, GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(pinFND, GPIO.OUT, initial=GPIO.HIGH)

Data = [0b00111111, 0b00000110, 0b01011011, 0b01001111,
        0b01100110, 0b01101101, 0b01111101, 0b00100111,
        0b01111111, 0b01101111, 0b01110111, 0b01111100,
        0b01011000, 0b01011110, 0b01111001, 0b01110001]

def fndDataOut(data):
    for i in range(8):
        GPIO.output(pinData[i], (data >> i) & 0x1)

def fnd_display(number):
    split = str(number)
    for i in range(len(split));
        GPIO.output(pinFND[i], GPIO.LOW)
        fndDataOut(Data)

try:
    while True:
        fnd_display(123456)
#         for i in range(len(Data)):
#             fndDataOut(Data[i])
#             time.sleep(0.5)

except KeyboardInterrupt:
    pass

finally:
    GPIO.cleanup()

"""
0 : 0b00111111
1 : 0b00000110
2 : 0b01011011
3 : 0b01001111

4 : 0b01100110
5 : 0b01101101
6 : 0b01111101
7 : 0b00100111

8 : 0b01111111
9 : 0b01101111
A : 0b01110111
B : 0b01111100

C : 0b01011000
D : 0b01011110
E : 0b01111001
F : 0b01110001
"""
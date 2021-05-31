import threading
import time

val = 0

def add_func():
    global val
    while True:
        val += 1
        time.sleep(0.01)
    
def sub_func():
    global val
    while True:
        val -= 1
        time.sleep(0.01)

t1 = threading.Thread(target=add_func)
t2 = threading.Thread(target=sub_func)

t1.start()
t2.start()

while True:
    print(val)
    time.sleep(0.5)

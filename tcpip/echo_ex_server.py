import socket
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.OUT, initial=GPIO.LOW)


server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_TCP)
server_socket.bind(('localhost', 9000))
server_socket.listen(socket.SOMAXCONN)

try:
    while True:
        client, addr = server_socket.accept()
        if not client:
            continue
        print("connected host: {} port: {}".format(addr[0], addr[1]))
        
        while True:
            try:
                recvmsg = client.recv(1024)
                if not recvmsg or len(recvmsg) == 0:
                    raise socket.error
            except:
                print("disconnectd")
                break
            client.send(recvmsg)
            
            print("from {} receive {}".format(addr, recvmsg.decode()))
            print(recvmsg, recvmsg.decode(), type(recvmsg), type(recvmsg.decode()))
           
            if recvmsg.decode() == "on":
                GPIO.output(11, GPIO.HIGH)
            elif recvmsg.decode() == "off":
                GPIO.output(11, GPIO.LOW)
                
except KeyboardInterrupt:
    pass
finally:
    server_socket.close()
    GPIO.cleanup()
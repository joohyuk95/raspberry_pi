import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_TCP)
client_socket.connect(("localhost", 9000))

try:
    while True:
        sendmsg = input()
        if sendmsg == 'q':
            break
        client_socket.send(sendmsg.encode())
        recvmsg = client_socket.recv(1024)
        print("received {}".format(recvmsg.decode()))

except KeyboardInterrupt:
    pass

finally:
    client_socket.close()

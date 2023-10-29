import socket
import socket
import time
from socket import AF_INET, SOCK_DGRAM,SOCK_STREAM,SHUT_RDWR
import threading
import sys
import os

def get_ip():
    my_ip=[(s.connect(('8.8.8.8', 53)), s.getsockname()[0], s.close()) for s in [socket.socket(socket.AF_INET, socket.SOCK_DGRAM)]][0][1]
    return my_ip

def get_dname():
    return socket.gethostname()

def receive_d():
    my_ip=get_ip()
    PORT_NUMBER = 5000
    SIZE = 1024
    message=""
    hostName = socket.gethostbyname( '0.0.0.0' )
    mySocket=socket.socket(AF_INET, SOCK_DGRAM)
    mySocket.bind( (hostName, PORT_NUMBER) )
    device_name=socket.gethostname()

    print("Test server listening on port {0}\n".format(PORT_NUMBER))
    out="Test server listening on port {0}\n".format(PORT_NUMBER)
   

    while True:
        (data,addr) = mySocket.recvfrom(SIZE)
        break

    print(data.decode('utf-8'))
    data=data.decode('utf-8')
    mySocket.close()

    otherSocket=socket.socket(AF_INET, SOCK_DGRAM)
    time.sleep(3)
    otherSocket.connect((data,PORT_NUMBER))
    otherSocket.send(device_name.encode('utf-8'))
    otherSocket.close()
    return "connecting"
    
def receive_out():
    SERVER_HOST = "0.0.0.0"
    SERVER_PORT = 5000
    BUFFER_SIZE = 4096
    SEPARATOR = "<SEPARATOR>"
    s = socket.socket()
    s.bind((SERVER_HOST, SERVER_PORT))
    s.listen(5)
    print(f"[*] Listening as {SERVER_HOST}:{SERVER_PORT}")
    client_socket, address = s.accept() 
    print(f"[+] {address} is connected.")
    received = client_socket.recv(BUFFER_SIZE).decode()
    filename, filesize = received.split(SEPARATOR)
    filename = os.path.basename(filename)
    filesize = int(filesize)
    with open(filename, "wb") as f:
        while True:
            bytes_read = client_socket.recv(BUFFER_SIZE)
            if not bytes_read:
                break
            f.write(bytes_read)

    client_socket.close()
    s.close()
    return "File received"

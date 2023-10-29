import socket

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

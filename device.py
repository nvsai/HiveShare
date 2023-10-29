import socket

def get_ip():
    my_ip=[(s.connect(('8.8.8.8', 53)), s.getsockname()[0], s.close()) for s in [socket.socket(socket.AF_INET, socket.SOCK_DGRAM)]][0][1]
    return my_ip

def get_dname():
    return socket.gethostname()


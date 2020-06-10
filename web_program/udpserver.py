from socket import *
from time import ctime

HOST = ''
PORT = 23333
BUFSIZ  = 1024
ADDR = (HOST, PORT)

udpSerSock = socket(AF_INET, SOCK_DGRAM)
udpSerSock.bind(ADDR)

while True:
    print('waiting for message...')
    data, addr = udpSerSock.recvfrom(BUFSIZ)
    print(data.decode(), addr)
    udpSerSock.sendto('[{}] {}'.format(ctime(), data).encode(), addr)
    print('...received from and returned to:', addr)

udpSerSock.close()

"""
output:
clien2 ('127.0.0.1', 57842)
...received from and returned to: ('127.0.0.1', 57842)
waiting for message...
clien1 ('127.0.0.1', 53288)
...received from and returned to: ('127.0.0.1', 53288)
waiting for message...

"""
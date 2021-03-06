from socket import *

HOST = 'localhost'
PORT = 23333
BUFSIZ  = 1024
ADDR = (HOST, PORT)
udpCliSock = socket(AF_INET, SOCK_DGRAM)

while True:
    data = input('> ')
    if not data:
        break
    udpCliSock.sendto(data.encode(), ADDR)
    data, addr = udpCliSock.recvfrom(BUFSIZ)
    if not data:
        break
    print(data.decode(), addr)

"""
> clien1
[Wed Jun 10 22:33:41 2020] b'clien1' ('127.0.0.1', 23333)
"""
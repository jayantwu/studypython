from socket import *
from time import ctime
HOST = ''
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST, PORT)
tcpSerSock = socket(AF_INET, SOCK_STREAM)
tcpSerSock.bind(ADDR)
tcpSerSock.listen(5)

while True:
    print("wating for connection...")
    tcpCliSock, addr = tcpSerSock.accept()
    print('...connected from:{}'.format(addr))
    while True:
        data = tcpCliSock.recv(BUFSIZ)
        if not data:
            break
        print('from_client> {}'.format(data.decode()))
        #tcpCliSock.send('[{}]:\n{}'.format(ctime(), input('>')).encode('utf-8'))
        tcpCliSock.send('[{}] {}'.format(ctime(), data).encode('utf-8'))
    tcpCliSock.close()

tcpSerSock.close()




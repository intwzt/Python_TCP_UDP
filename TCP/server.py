#coding=utf-8
import socket
import threading
import time


def tcplink(sock, addr):
    print 'Accept new connection from %s:%s...' % addr
    sock.send('Welcome!')
    while True:
        data = sock.recv(1024)
        time.sleep(1)
        if(data == 'exit' or not data):
            break
        sock.send('Hello %s' % data)
    sock.close()
    print 'Connection from %s:%s closed.' % addr

#建立socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#监听端口
s.bind(('127.0.0.1', 9999))
#设置最大连接数
s.listen(5)
print 'Waiting for connection...'

while True:
    #等待一个新的连接
    sock, addr = s.accept()
    #创建一个新的线程来处理TCP连接
    t = threading.Thread(target=tcplink, args=(sock, addr))
    t.start()
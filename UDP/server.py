#coding=utf-8

import socket
import threading
import time

def udplink(data, addr, s):
    time.sleep(1)
    print 'Received from %s:%s.' % addr
    s.sendto('Hello, %s!' % data, addr)


#创建socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

#绑定端口
s.bind(('127.0.0.1', 9999))
print 'Bind UDP on 9999...'
while True:
    #接收数据
    data, addr = s.recvfrom(1024)
    t = threading.Thread(target=udplink, args=(data, addr, s))
    t.start()

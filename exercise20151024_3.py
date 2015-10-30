#!/usr/bin/env python
# coding: utf-8
### exercise20151024_3.py
'''
用socket与服务器交互通信
客户端输入：
nc 127.0.0.1 55667
'''
import socket
import time

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) #默认0，地址不重用；设置为1，重用。

s.bind(("127.0.0.1",55667))     #绑定服务器地址：端口

s.listen(5)
print "waiting for connection..."

sock, addr = s.accept()
sock.send("Welcome! \n")

while True:
    data = sock.recv(1024)
    time.sleep(1)
    if data.strip() == "exit":
        close = True
        break
    sock.send("Hello, %s!" % data)

if close:
    sock.close()
    print "Connection from %s:%s closed." % addr


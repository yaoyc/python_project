#!/usr/bin/env python
# coding: utf-8
### exercise20151024_2.py
'''
用socket向服务器发送信息，抓取服务器信息
'''
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect(("www.baidu.com", 80))    #连接服务器地址：端口

print s.send("GET / HTTP/1.1\r\nHost: www.baidu.com\r\n#Connection: close\r\n\r\n")

print "*" * 20

buffer = []

while True:
    d = s.recv(1024)
    if d:
        buffer.append(d)
    else:
        break
data = "".join(buffer)  #将列表信息拼接
print data

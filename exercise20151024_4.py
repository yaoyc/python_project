#!/usr/bin/env python
# coding: utf-8
### exercise20151024_4.py
'''
程序用socket实现 nc 连接功能
'''
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect(("127.0.0.1",55667))

print s.recv(1024)
for data in ["1xf", "dc", "world"]:
    s.send(data)
    print s.recv(1024)

s.send("exit")
s.close()

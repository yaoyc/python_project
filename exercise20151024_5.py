#!/usr/bin/env python
# coding: utf-8
### exercise20151024_5.py
'''
用requests 模块获取网站信息
'''
import requests
URL = "http://tieba.baidu.com/p/2460150866"

r = requests.get(URL)
r.headers
r.status_code
#r.test

print r.content

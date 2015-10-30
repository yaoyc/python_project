#!/usr/bin/env python
# coding: utf-8
### exercise20151024_5.py
'''
用requests 模块获取网站信息
'''
import requests

r = requests.get("http://www.baidu.com")
r.headers
r.status_code
#r.test
print r.content

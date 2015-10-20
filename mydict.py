#!/usr/bin/env python
# coding:utf-8
### mydict.py
"""
自定义模块，被exercise20151017_4.py调用
功能类似于 字典
"""

class Dict(dict):
    """docstring for Dict"""
    def __init__(self, **kv):
        super(Dict, self).__init__(**kv)
    
    def __getatter__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Dict' object has no atteribute '%s'" %key)

    def __setatter__(self, key, value):
        self[key] = value

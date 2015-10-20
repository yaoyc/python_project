#!/usr/bin/env python
# coding:utf-8
### exercise20151017_4.py
"""
单元测试
测试自定义模块 mydict.py
"""


import unittest     #编写单元测试须引入此模块
from mydict import Dict     #待测试模块程序

class TestDict(unittest.TestCase):
    """docstring for TestDict"""
    def test_init(self):
        d = Dict(a=1, b='test')
        self.assertEqual(d.a, 1)
        self.assertEqual(d.b, 'test')
        self.assertTrue(isinstance(d, dict))

    def test_key(self):
        d = Dict()
        d.key = 'value'
        self.assertTrue("key" in d)
        self.assertEqual(d['key', 'value'])

    def test_attr(self):
        d = Dict()
        d.key = "value"
        self.assertTrue("key" in d)
        self.assertEqual(d["key"], "value")

    def test_keyerror(self):
        d = Dict()
        with self.assertRaises(KeyError):
            value = d["empty"]

    def test_attrerror(self):
        d = Dict()
        with self.assertRaises(AttributeError):
            value = d.empty

if __name__ == '__main__':
    unittest.main()

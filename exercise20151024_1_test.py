#!/usr/bin/env python
# coding: utf-8
### exercise20151024_1_test.py
'''商品定价，测试用例。'''
import unittest
from exercise20151024_1 import Everyday_deco,Weekend_deco,pricing,price

class TestPrice(unittest.TestCase):
    """docstring for TestPrice"""
    def test_init(self):
        d = pricing(HUAWEI=3000, Iphone=5288, Thinkpad=7000)
        self.assertEqual(d["HUAWEI"], "2380.00")

if __name__ == '__main__':
    unittest.main()

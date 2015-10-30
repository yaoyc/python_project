#!/usr/bin/env python
# coding: utf-8
### exercise20151024_1_test.py
'''
商品定价，测试用例。
'''
import unittest
from exercise20151024_1 import *

class TestPrice(object):
    """docstring for TestPrice"""
    def test_init(self):
        d = pricing(HUAWEI=3000, Iphone=5288, Thinkpad=7000)
        self.assertEqual(d.HUAWEI, 3000)
        self.assertEqual(d.Iphone, 5288)
        self.assertEqual(d.Thinkpad, 7000)
        self.assertTrue(isinstance(d, dict))

    def test_error(self):
        with self.assertRaises(TypeError):
            pricing(HUAWEI=3000)
            pricing("HUAWEI")
if __name__ == '__main__':
    unittest.main()

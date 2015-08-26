#! /usr/bin/env python3
#-*- coding:utf-8 -*-

'单元 测试 方法'

__author__='chenmd'

import unittest

from mydict import Dict

class TestDict(unittest.TestCase):
	def test_init(self):
		d=Dict(a=1,b='test')
		self.assertEqual(d.a,1)
		self.assertEqual(d.b,'test')
		self.assertTrue(isinstance(d,dict))
		self.assertTrue(isinstance(d,Dict))
	
	def test_keyerror(self):
		d=Dict()
		with self.assertRaises(KeyError):
			value=d['empty']


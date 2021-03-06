#! /usr/bin/env python3
#-*- coding:utf-8 -*-

'单元 测试 方法'

__author__='chenmd'

#要测试的类
class Dict(dict):
	def __init__(self,**kw):
		super().__init__(**kw)
	
	def __getattr__(self,key):
		try:
		 return self[key]
		except KeyError:
			raise AttributeError(r"'Dict' object has no attribute '%s'"%key)
	def __setattr__(self,key,value):
		self[key]=value


#! /usr/local/env python3
#-*- coding:utf-8 -*-

' a test module '

__author__='chenmd'

import sys

def test():
	args=sys.argv
	if len(args)==1:
		print("hello word")
	elif len(args)==2:
		print("hello:",args[1])
	else:
		print("Too many arguments")

class Hello(object):
	def sayHello(self,name):
		print("hello word:",name)
		

if __name__=='__main__':
	test()
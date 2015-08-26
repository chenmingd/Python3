#! /usr/bin/env python3
#-*- coding:utf-8 -*-

'异常 错误 调试'
try:
	num=10/0

except Exception as e:
	print("error :",e)

finally:
	print("finally run")

print("end")


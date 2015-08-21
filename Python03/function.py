#! /usr/bin/env python3
# -*- coding:utf-8 -*-
import math
#函数的使用
def my_abs(x):
	if not isinstance(x,(int,float)):
		raise TypeError("bad operand type")
	if(x>0):
		return x;
	else:
		return -x;
print(my_abs(-2),my_abs(3))
#print(my_abs('z'))

def move(x,y):
	return x-y,y-x

print(move(3,4))

def quadratic(a,b,c):
	righType=(int,float)
	if not isinstance(a,righType) or not isinstance(b,righType) or not isinstance(c,righType):
		raise TypeError("type error")
	return "%dx2+%dx+%d"%(a,b,c)
print(quadratic(1,2,3))

#注意默认参数必须指向不变对象

def person(name,sex,age=6,city="北京"):
	return "姓名%s,性别%s,年龄%s,城市%s"%(name,sex,age,city)

print(person("chen","nan",8))
print(person("chen","nan",city='上海'))

def cal(*numbers):
	sum=0
	for num in numbers:
		sum+=num
	return sum

print(cal(*(1,2,3)))

#关键参数
def person(name,sex,**other):
	print("name:",name,"sex:",sex,"other:",other)
	
person("陈","男")

	
person("陈","男",city="北京",school="大学")

tuplee={"city":"city","school":"school"}

person("chen","nan",**tuplee)

#汉诺塔
def hnt(n,A,B,C):
	if(n==1):
		print("%s-->%s"%(A,C))	
	else:
		hnt(n-1,A,C,B)
		hnt(1,A,B,C)
		hnt(n-1,B,A,C)
hnt(10,"A","B","C")
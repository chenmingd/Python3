#! /usr/bin/env python3
#-*- coding:utf-8 -*-

class Person(object):
	#类的变量
	discript="discript" 
	
	#相当于构造方法
	def __init__(self,pwd):
		self.__pwd=pwd
		self.pwd=pwd+10
		print(self,pwd,self.__pwd)
	def say(self,name):
		print("hello:"+name)
	def hello():
		print("hello()")
	def sayPwd(self):
		print(self.__pwd,"cd")
		print("####")
#Person.hello();
print("##########################")
person =Person(10)
#person.say("chenmd")
#person.hello()
#print(person.__pwd)
#print(person.pwd)
print(person.sayPwd())
print(123,person)

class Student(Person):
	pass
	
stu=Student(10)
stu.say("")

print(type(stu))

print(stu.discript+":"+Student.discript+":"+Person.discript)

print("####################################################")
print(dir(stu))
print(stu.__sizeof__())

#面向对象高级编程

stu1=Student(20)
stu.sc="123"
#print(stu1.sc+":"+stu.sc)
print(stu.sc)

def printInfo(self):
	print("self:",self)
from types import MethodType
stu.printInfo=MethodType(printInfo,stu)
stu.printInfo()
#stu1.printInfo()
Person.printInfo=MethodType(printInfo,Person)
stu1.printInfo()
Student.printInfo=MethodType(printInfo,Student)
stu1.printInfo()
del Student.printInfo
stu1.printInfo()
del Person.printInfo
#stu1.printInfo()


print("$#################################$")
#请利用@property给一个Screen对象加上width和height属性，以及一个只读属性resolution
class Screen(object):
	@property
	def width(self):
		return self._width
		
	@width.setter
	def width(self,value):
		if not isinstance(value,int):
			raise TypeError("type errot require int")
		else:
			self._width=value
			
	@property
	def height(self):
		return self._height
		
	@height.setter
	def height(self,value):
		if not isinstance(value,int):
			raise TypeError("type errot require int")
		else:
			self._height=value
	
	@property
	def resolution(self):
		return [self._width,self._height]
		
screen=Screen()
screen.width=100;
screen.height=200;
print(screen.width,screen.height)
print(screen.resolution)


#定制类的开发
print("###########定制类的开发###########")
class Spacial(object):
	def __init__(self,num=100,step=5):
		self.num=num
		self.step=step
		
	@property
	def num(self):
		return self.__num
	
	@num.setter
	def num(self,value):
		if not isinstance(value,int):
			raise TypeError("type error require int")
		else:
			self.__num=value
	@property
	def step(self):
		return self.__step
	
	@step.setter
	def step(self,value):
		if not isinstance(value,int):
			raise TypeError("type error require int")
		else:
			self.__step=value
			
	def __str__(self):
			return "spacial num:%d,step:%d"%(self.num,self.step)
		
	__repr__=__str__
	
	def __iter__(self):
		return self
	
	def __next__(self):
		if self.num<=0:
			raise StopIteration()
		self.num=self.num-self.step
		return self.num
	
spacial=Spacial()
print(spacial.num,spacial.step,spacial)

'''
for n in spacial:
	print(n)
'''
l=[x for x in spacial]
print(l)


#这个代码牛逼
class Chain(object):

	def __init__(self, path=''):
		self._path = path

	#一个链式定义的好例子
	def __getattr__(self, path): 
		return Chain('%s/%s' % (self._path, path))

	def __str__(self):
		return self._path

	__repr__ = __str__
print( Chain())
print( Chain().status)
print( Chain().status.user.timeline.list)


#枚举
from enum import Enum,unique
Month=Enum("Month",('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))
print(Month.Jan.value)

@unique
class WeekDay(Enum):
	Sun = 0 # Sun的value被设定为0
	Mon = 1
	Tue = 2
	Wed = 3
	Thu = 4
	Fri = 5
	Sat = 6
print("WeekDay Sun",WeekDay.Sun.value,WeekDay['Sun'].value)
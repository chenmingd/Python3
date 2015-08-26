#! /usr/bin/env python3
#-*- coding:utf-8 -*-

#函式编程

#高阶函数
#map函数接收2个参数一个函数，一个是Iterable 比如 f(x)=x*x;map将传入的函数依次作用到序列的每个元素，并把结果作为新的Iterator返回
def f(x):
	if not isinstance(x,int):
		raise TypeError("type error plean type int or float param")
	return x*x

#mp=map(f,[x for x in range(10)])
mp=map(f,(x for x in range(10)))
print(mp,list(mp))

#reduce函数reduce把一个函数作用在一个序列[x1, x2, x3, ...]上，这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算
from functools import reduce
def add(x,y):
	return x+y

reducee=reduce(add,(x for x in range(3)))
print(reducee)


def str2int(s):
    def fn(x, y):
        return x * 10 + y
    def char2num(s):
        return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]
    return reduce(fn, map(char2num, s))

print(str2int("123976"))


names=['adam', 'LISA', 'barT'] #首字母大写其余的小写
def f(name):
	return name[0:1].upper()+name[1:].lower()

mp=map(f,names)
print(list(mp))

print([x[0:1].upper()+x[1:].lower() for x in names])  #首字母大写其余的小写
print(list(map(lambda x:x[0:1].upper()+x[1:].lower(),names)))  #首字母大写其余的小写

prod=reduce(lambda x,y:x*y,list(range(1,4))) #list每一个数相乘
print(prod)

#filter()把传入的函数依次作用于每个元素，然后根据返回值是True还是False决定保留还是丢弃该元素。
g=filter(lambda x:x%2==0,(x for x in range(20)))
'''
print(list(g))
while True:
    try:
        x = next(g)
        print('g:', x)
    except StopIteration as e:
        print('Generator return value:', e.value)
        break
'''	
for num in g:
	print(num)
	
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
l=sorted(L,key=lambda x:x[0].lower())
print(l)
		
l=sorted(L,key=lambda x:x[1])
print(l)

l=sorted(L,key=lambda x:x[1],reverse=True)
print(l)

#一个很好的例子
L = [[1,2],[3,4],[5,6],[7,8]];
print([(lambda x : x[0]*x[0]+x[1]*x[1])(x) for x in L]);

#装饰器
def log(func):
	def wrapper(*args,**kw):
		print("run %s()"%(func.__name__))
		return func(*args,**kw)
	return wrapper

@log  #要用log装饰newfun函数
def newfun(a,b,c):
	return a+b+c
tn=newfun(1,2,3)
print("newfun result:"+str(tn))


#通用的log装饰函数
import functools 
def commonlog(text):
	if isinstance (text,str):
		def decorator(func):
			@functools.wraps(func)
			def wrapper(*args,**kw):
				print("before call log %s__call %s()"%(text,func.__name__))
				rect=func(*args,**kw)
				print("end call and result is",rect,sep=":")
				return rect
			return wrapper
		return decorator
	else:
		def wrapper(*args,**kw):
			print("log %s__call %s()"%(text,text.__name__))
			print("before call")
			rect=text(*args,**kw)
			print("end call")
			return rect
		return wrapper
		
@commonlog("xxx")
def newtest(a,b,c):
	return a+b+c
print("result is %d"%(newtest(1,2,3)))

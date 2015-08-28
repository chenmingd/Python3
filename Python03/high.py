#! /usr/bin/env python3
#-*- coding:utf-8 -*-
#slice
print((list(range(100))[0:50:2]))
print("ABCDEFGHIJKLMNOPQRSTUVWXYZXYZNYCICANSEEMYABC"[1:20])



#Iteration
l=list(range(10))
print(l)
for num in l:
	print(num)
l=(range(10))
print(l)
for num in l:
	print(num)
	
dictt={"key1":"key1","key2":"key2","key3":"key3","key4":"key4","key5":"key5"}
for key in dictt:
	print(key)
for value in dictt.values():
	print(value)
for item in dictt.items():
	print(*item)
from collections import Iterable
print(isinstance(item,Iterable))



#List Comprehensions
l=list(range(100))[0:5]
print(l)
l=[x*x for x in range(3)] #[0*0,1*1,2*2]
print(l)
l=[x*x for x in range(1,11)] #[1*1,2*2,3*3,...,10*10]
print(l)
l=[x*x for x in range(1,11) if x%2==0]
print(l)

ll=['A','B','C']
l=[m+n for m in "123" for n in ll]
print(l)

l=["123"+n for n in ll]
print(l)

L = ['Hello', 'World', 18, 'Apple', None]
ll=[it.lower() for it in L if isinstance(it,str)] #过滤出所有的字符串并全部小写
print(ll) 
ll=[it.lower() if isinstance(it,str) else it for it in L] #将列表中的所有字符串全部小写
print(ll)



#generator如果列表元素可以按照某种算法推算出来，那我们是否可以在循环的过程中不断推算出后续的元素呢？这样就不必创建完整的list，从而节省大量的空间。在Python中，这种一边循环一边计算的机制，称为生成器：generator
g=(x*x*x for x in range(5))
for x in g:
	print(x)
print("#########################################")
	
def fbl(max): #斐波拉数列
	n,a,b=0,0,1
	while n<max:
		print(b)
		a,b=b,a+b
		n=n+1
	return 'done'
fbl(10)
print(fbl)

def fbl(max): #斐波拉数列
	n,a,b=0,0,1
	while n<max:
		yield b
		a,b=b,a+b
		n=n+1
	return 'done'

print(fbl(6))

for num in fbl(6):
	print(num)
l=[1,2,3,4]
print(l[0:])

print("###################")

l=[1,2,3,4]
l=l+[1,2,3,4]
print(l)
print("####################")
def triangles_1():  #杨辉三角的写法一
	l=[1]
	while True:
		yield l
		l=[l[x]+l[x+1] for x in range(len(l)-1)]
		l.insert(0,1)
		l.append(1)


n=0
for num in triangles_1():
	print(num)
	n=n+1
	if n%10==0:break
	
def triangles_2(): #杨辉三角的写法二
	l1,l,l2=[1,0],[1],[0,1]
	yield l
	while True:
		l=[l1[x]+l2[x] for x in range(len(l1))]
		l1,l2=[0]+l,l+[0]
		yield l

n=0
for num in triangles_2():
	print(num)
	n=n+1
	if n%10==0:break
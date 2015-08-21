#!/usr/bin/env python3
# -*- coding:utf-8 -*-
print('Hello','word')
#name=input("请输入你的姓名：")
name='陈明东'
age=25
print("你好%d岁的%s"%(int(age),name)) #格式化输出
print("name的长度是",len(name),sep=":") #字符串的长度
print("name的bytec长度是",len(name.encode("utf-8")),sep=":") #byte长度
classmates=["cmd","zjk","zy"] #数组
print("数组classmates",classmates)
classmate=classmates.pop();
print(classmates,len(classmates))
classmates.append(classmate)
print(classmates,len(classmates))
for classmate in classmates:
	print(classmate)
	print(len(classmates))

#list tuple 测试
L = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', 'Ruby', 'PHP'],
    ['Adam', 'Bart', 'Lisa']
]
print("打印出apple,Python,Lisa",L[0][0],L[1][1],L[2][2],sep=":")

#求和
sum=0
for x in range(4):
	sum+=x
print(sum)

######
a=0
r=input('1+2+...+')
r=int(r)
for x in range(r):
	a=a+x
a=int(a)
print('a=',a,sep="")
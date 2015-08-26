#! /usr/bin/env python3
#-*- coding:utf-8 -*-

'IO的读写'
with open('d:/data/1.txt',"r") as f:
	print(f.read())
	f.close()
print("############################################")
	
#如果文件很小，read()一次性读取最方便；如果不能确定文件大小，反复调用read(size)比较保险；如果是配置文件，调用readlines()最方便
with open('d:/data/db.properties',"r") as f:
	for line in f.readlines():
		print(line.strip())  # 把末尾的'\n'删掉
		#print(line)
	f.close();
	
print("############################################")
with open('d:/data/db.properties',"r") as f:
	while True:
		line=f.readline();
		if line=='':break
		print(line.strip())
	f.close();

'''
很多时候，数据读写不一定是文件，也可以在内存中读写。
StringIO顾名思义就是在内存中读写str
'''
print("############################################")
from io import StringIO
sio=StringIO()
sio.write('hello ')
sio.write('word')
print(sio.getvalue())

print("############################################")
sio=StringIO("Hello!\nHi\npoppy");
while True:
	line=sio.readline()
	if line=='':break
	print(line.strip())
	
print("############################################")

from io import BytesIO
bio=BytesIO()
bio.write('中国'.encode('utf-8'))
print(bio.getvalue())

print("##################操作文件和目录##########################")
import os
print("操作系统内核：%s"%os.name)
#print("操作系统环境变量：%s"%os.environ)
#print("操作系统环境变量PATH：%s"%os.environ.get("PATH"))

print(os.path.abspath('.'))
print(os.path.abspath('..'))
print(os.path.abspath('d:\data'))
#path=os.path.join('d:\data','testdir')
#print(path)
#os.mkdir(path)

print("###################当前目录中所有的python文件##########################")
l=[x for x in os.listdir(".") if os.path.isfile(x) and os.path.splitext(x)[1]=='.py']
print (l)


print("#############################################################################")

	
def listfile(path,name):
	fs=(x for x in os.listdir(path))
	for f in fs:
		if os.path.isfile(f) and os.path.splitext(f)[1]==name:
			print(os.path.join(path,f))
		elif os.path.isdir(f):
			listfile(os.path.join(path,f),name)
		else:
			pass

#listfile(".",".py")


print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
def findfile(name,path='.'):
    print('path : %s'%path)
    pwd = os.path.abspath(path)
    print(os.listdir(pwd))
    for f in os.listdir(pwd):
        if os.path.isdir(f):
            findfile(name,f)
        if os.path.isfile(f) and (name in os.path.split(f)[1]):
            print('The file in:')
            print(os.path.join(pwd,f))

#findfile("py")

print("###########################################")
def listff(find_str):
	for root,dirs,files in os.walk(os.getcwd()):
		for f in files:
			if f.find(find_str) != -1:
				print(root + os.sep + f)
#listff("py")

print("###########################################")
with open("d:/data/access.log","r") as f:
	lines=[x for x in f.readlines() if x.find('2bE235BG')>-1]
	print(len(lines))
	#for line in lines:
	with open("d:/data/tmp.log","w") as f1:
		f1.writelines(lines);
		f1.close()
		#print(line)
	f.close()
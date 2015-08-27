#! /usr/bin/env python3
#-*- coding:utf-8 -*-

'多线程'
'''
多任务的实现有3种方式：

多进程模式；
多线程模式；
多进程+多线程模式。
'''


#下面是多进程的方案书写

'''
Unix/Linux操作系统提供了一个fork()系统调用，它非常特殊。普通的函数调用，调用一次，返回一次，
但是fork()调用一次，返回两次，因为操作系统自动把当前进程（称为父进程）复制了一份（称为子进程），
然后，分别在父进程和子进程内返回。
'''
import os,sys

'''
print("#####################################")
if len(sys.argv)>1:
	print("Process (%s) start...%s>>"%(os.getpid(),sys.argv[1]))
else:
	print("Process (%s) start..."%os.getpid())
	print(sys.argv)
'''
#windows平台不支持fork
'''
由于Windows没有fork调用，上面的代码在Windows上无法运行。由于Mac系统是基于BSD（Unix的一种）内核，所以，在Mac下运行是没有问题的
有了fork调用，一个进程在接到新任务时就可以复制出一个子进程来处理新任务，
常见的Apache服务器就是由父进程监听端口，每当有新的http请求时，就fork出子进程来处理新的http请求
'''
if os.name!='nt':
	pid=os.fork()
	if pid==0:
		print('I am child process (%s) and my parent is %s.' % (os.getpid(), os.getppid()))
	else:
		print('I (%s) just created a child process (%s).' % (os.getpid(), pid))

#跨平台多进程解决方案
from multiprocessing import Process
def run_proc(name): #子进程
	print("Run child process %s id:%s pid:%s"%(name,os.getpid(),os.getppid()))

if __name__=="__main__":
	print("Parent process %s..."%os.getpid())
	p=Process(target=run_proc,args=('test',)) #子进程是本身
	print("child process will start")
	p.start()
	p.join()
	print("child process end.")

#线程池
import time,random
from multiprocessing import Pool
def long_time_task(name):
	print("child process %s(%s,%s) run"%(name,os.getpid(),os.getppid()))
	start=time.time()
	time.sleep(random.random()*3)
	end=time.time()
	print("Tast %s runs %0.2f seconds."%(name,end-start))
if __name__=="__main__":
	print("Parent process %s"%os.getpid())
	p=Pool(5)
	for i in range(10):
		p.apply_async(long_time_task,args=(i,)) #子进程是本身
	print("Waiting for all Processing done...")
	p.close()
	p.join()
	print('All subprocesses done.')

#子进程不是本身
import subprocess

print("nslookup rrs.focushow.cn")
r=subprocess.call("nslookup rrs.focushow.cn")
print("Exit code:%d"%r)


#进程间的通信
#Process之间肯定是需要通信的，操作系统提供了很多机制来实现进程间的通信。
#Python的multiprocessing模块包装了底层的机制，
#提供了Queue、Pipes等多种方式来交换数据
from multiprocessing import Process,Queue
import os,time,random

def write(q):
	print("Process %s write to queue"%os.getpid())
	for value in ['A','B','C','A','B','C','Q']:
		print("put %s in queue"%value)
		q.put(value)
	time.sleep(random.random())
def read(q):
	print("Process %s read from queue"%os.getpid())
	while True:
		value=q.get(True)
		print("get %s from queue"%value)
		if value=="Q":
			break

if __name__=="__main__":
	q=Queue()
	pw=Process(target=write,args=(q,))
	
	pw.start()
	pr.start()
	
	pw.join()
	#pr.terminate()
	pr.join()

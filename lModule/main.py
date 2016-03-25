# -*- coding: utf-8 -*-
# @Date    	: 2016-03-24 16:27:46
# @Author  	: mr0cheng
# @email	: c15271843451@gmail.com
'''
Sub module main.py file achieve login function.
'''

import os,sys,time

log	=os.path.join(sys.path[0],'log')

__file__ = os.path.abspath(__file__)
if os.path.islink(__file__):
    __file__ = getattr(os, 'readlink', lambda x: x)(__file__)

current_path = os.path.dirname(os.path.abspath(__file__))
sys.path.append(current_path)
from login import login

'''
params:
	u 	:username
	p 	:password
	c 	:the path of cookie
'''
def main(u,p,c):
	sysLog({'time':time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))})
	t 	=''
	l 	=login(u,p,c)
	return l.login()

'''
params:
	d 	:dict
	f 	:written file
'''
def sysLog(d,f 	=log):
	f=open(f,'a',encoding 	='utf-8')
	for i in d:
		f.write(i+':'+str(d[i])+'\n')
	f.close()


if __name__=='__main__':
	print(sys.path)
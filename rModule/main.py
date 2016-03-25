# -*- coding: utf-8 -*-
# @Date    	: 2016-03-25 16:32:42
# @Author  	: mr0cheng
# @email	: c15271843451@gmail.com

'''
Sub module main.py file achieve retweet function.
'''

import os,sys,time

__file__ = os.path.abspath(__file__)
if os.path.islink(__file__):
    __file__ = getattr(os, 'readlink', lambda x: x)(__file__)

current_path = os.path.dirname(os.path.abspath(__file__))
sys.path.append(current_path)
from search import search
from retweet import retweet

log	=os.path.join(sys.path[0],'log')
ret =os.path.join(sys.path[0],'retweet')
web =os.path.join(sys.path[0],'weibo.csv')

'''
params:
	t 	:Keyword search
	p 	:the page num
	c 	:cookie file
'''
def main(t,p,c):
	rt={}
	rt['time']=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
	state,rst=getOneWeibo()
	if state is False:
		sh 	=search(t,p,c)
		state,js 	=sh.search()
		if state:
			rt['response of search']=js
			setWeiboList(js)
		state,rst=getOneWeibo()
	if state is False:
		sysLog({'oneWeibo':'No more weibo to retweet!'})
		print('No more weibo to retweet!')
		return False
	rt['the detail infomation of retweeted weibo']=rst
	rt=retweet(rst['mid'],rst['reason'],c)
	state,rsp=rt.retweet()
	rt['response of retweet']=rsp
	sysLog(rt)
	if state:
		with open(ret, 'a') as f:
			f.write(rst['mid']+',')
			f.close()
	return state
	

def getOneWeibo():
	pass

'''
write the weibo list into `weibo` file,include:
	follow 	:
	mid 	:
	url of follow 	:

'''
def setWeiboList(js):
	pass

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
	pass


'''
@微博抽奖平台
关注@smalltail小尾巴 转发此微博并@3位好友 
31号抽出
艾特两个好友
关注店主@ALIN-STUDIO 并转发这条微博 @ 三个真实好友
'''

'''
refer_flag=1001030103
mid
'''
# -*- coding: utf-8 -*-
# @Date    	: 2016-03-24 10:12:40
# @Author  	: mr0cheng
# @email	: c15271843451@gmail.com

import sys,os
import lModule.main as lm
import rModule.main as rm
import fModule.main as fm
import time

cookie	=os.path.join(sys.path[0],'config','cookie')
log	=os.path.join(sys.path[0],'log')
u=''	#username
p=''	#password

def retweet():
	fm.main(cookie,rm.main(cookie))
def main():
	if lm.main(u,p,cookie):
		retweet()
if __name__=='__main__':
	startTime=time.time()
	main()
	print('finish total time:',time.time()-startTime)

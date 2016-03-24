# -*- coding: utf-8 -*-
# @Date    	: 2016-03-24 10:12:40
# @Author  	: mr0cheng
# @email	: c15271843451@gmail.com

import sys,os

cookie	=os.path.join(sys.path[0],'config','cookie')
log	=os.path.join(sys.path[0],'log')

class start(object):
	u=''	#username
	p=''	#password
	def __init__(self,flag):
		self.flag	=flag
	
	def g(self):
		f 	=self.flag
		if f==0:
			u()	#unfollow
		elif f==1 or f==2:
			rst,dt=g()
			if rst if True:
				r()	#retweet 
			g()	#get one weibo infomation
			

'''
params:
	d:dict
	f:written file
'''
def sysLog(d,f 	=log):
	f=open(f,'a',encoding 	='utf-8')
	for i in d:
		f.write(i+':'+str(d[i])+'\n')
	f.close()

def main():
	import random,time
	flag	=random.randint(0,7)
	print('flag:',flag)
	sysLog({'time':time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))+'\tflag:'+str(flag)})
	st 	=start(flag)
	rt 	=st.g()

if __name__=='__main__':
	main()
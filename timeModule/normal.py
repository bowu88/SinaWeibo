# -*- coding: utf-8 -*-
# @Date    	: 2016-04-17 22:03:58
# @Author  	: mr0cheng
# @email	: c15271843451@gmail.com

#http://docs.scipy.org/doc/numpy/reference/generated/numpy.random.normal.html

import numpy as np
import matplotlib.pyplot as plt
import sys,os
#PEOPLE NEED HAVE A REST FOR EIGHT HOURS ^.^! 
#6:00am - 22:00pm
WORK_HOURS=16
SCHEDULE_FILE=os.path.join(sys.path[0],'schedule')

def normalDay():
	mu=WORK_HOURS*12
	sigma=30
	return np.random.normal(mu,sigma,1000)
'''
@times:fresh weibo times(positive integer) during one day.
'''
def normalMinutes(times):
	mu=WORK_HOURS*60//times
	sigma=mu//3		#smaller is not lower than 1/3 of your life.
	return np.random.normal(mu,sigma,times)

def saveSchedule(r):
	with open(SCHEDULE_FILE,'a') as f:
		f.write(','.join(str(int(x)) for x in r))
		f.write('\n')
def update_schedule():
	s=normalDay()
	for i in s:
		r=normalMinutes(round(i))
		saveSchedule(r)

if __name__=='__main__':
	update_schedule()
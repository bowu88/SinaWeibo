# -*- coding: utf-8 -*-
# @Date    	: 2016-03-25 16:36:50
# @Author  	: mr0cheng
# @email	: c15271843451@gmail.com

import urllib
from urllib import parse
import http.cookiejar
class search(object):

	headers={
			'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:44.0) Gecko/20100101 Firefox/44.0',
		}

	def __init__(self,t,p,c):
		self.u 	='http://s.weibo.com/weibo/'+urllib.parse.quote(urllib.parse.quote(t.encode('utf-8')))+'&b=1&page='+str(p)

		self.cj=http.cookiejar.LWPCookieJar(c)
		self.cookie_support=urllib.request.HTTPCookieProcessor(self.cj)
		self.opener=urllib.request.build_opener(self.cookie_support,urllib.request.HTTPHandler)
		urllib.request.install_opener(self.opener)
		self.cj.load(ignore_discard=True, ignore_expires=True)

	def search(self):
		rst 	=urllib.request.Request(url=self.u,headers=self.headers)
		rsp 	=urllib.request.urlopen(rst).read()
		try:
			rsp=rsp.decode('utf-8')
		except:
			rsp=rsp.decode('gbk')
		return rsp

if __name__=='__main__':
	t='转发抽奖'
	url='http://s.weibo.com/weibo?%s'
	s=urllib.parse.quote(urllib.parse.quote(t.encode('utf-8')))
	print(type(s))
# -*- coding: utf-8 -*-
# @Date    	: 2016-03-25 21:14:43
# @Author  	: mr0cheng
# @email	: c15271843451@gmail.com
import urllib,re
from urllib import parse
import http.cookiejar
class retweet(object):
	u='http://s.weibo.com/ajax/mblog/forward?__rnd=1458911498912'
	headers={
		'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:44.0) Gecko/20100101 Firefox/44.0',
		'Referer':'http://s.weibo.com/weibo/%25E8%25BD%25AC%25E5%258F%2591%25E6%258A%25BD%25E5%25A5%2596&b=1&page=2'
		}
	'''
	m 	:mid
	r 	:reason
	'''
	def __init__(self,m,r,c):
		self.cj=http.cookiejar.LWPCookieJar(c)
		self.cookie_support=urllib.request.HTTPCookieProcessor(self.cj)
		self.opener=urllib.request.build_opener(self.cookie_support,urllib.request.HTTPHandler)
		urllib.request.install_opener(self.opener)
		self.cj.load(ignore_discard=True, ignore_expires=True)
		self.form={
			'appkey':'',
			'mid':m,
			'style_type':'1',
			'reason':r,
			'location':'',
			'_t':'0'
		}

	def retweet(self):
		post_data=urllib.parse.urlencode(self.form).encode(encoding='utf-8')
		rst=urllib.request.Request(url=self.u,data=post_data,headers=self.headers)
		rsp=urllib.request.urlopen(rst).read()
		rst=re.findall('"code":"(\d*)"',str(rsp))
		if rst and rst[0]=='100000':
			print('retweet successfully!')
			return True,rsp
		print('retweet fail!')
		return False,rsp

if __name__=='__main__':
	c='D:\\workspace\\python\\SinaWeibo\\config\\cookie'
	rt=retweet('3952898134646376','@逗兜5580956781 @sds',c)
	state,rsp=rt.retweet()
	if state:
		pass
	else:
		print(rsp)

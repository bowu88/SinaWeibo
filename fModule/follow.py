# -*- coding: utf-8 -*-
# @Date    	: 2016-03-28 21:38:10
# @Author  	: mr0cheng
# @email	: c15271843451@gmail.com

import urllib,re,time
from urllib import parse,request
import http.cookiejar
import requests

class follow(object):
	headers={
			'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:44.0) Gecko/20100101 Firefox/44.0',
		}
	def __init__(self,c):
		self.cj=http.cookiejar.LWPCookieJar(c)
		self.cookie_support=urllib.request.HTTPCookieProcessor(self.cj)
		self.opener=urllib.request.build_opener(self.cookie_support,urllib.request.HTTPHandler)
		urllib.request.install_opener(self.opener)
		self.cj.load(ignore_discard=True, ignore_expires=True)

	def getForm(self,u):
		t=''
		r=requests.get(url=u,cookies=self.cj)
		if r.url==u:
			t=r.text
		else:
			r=requests.get(url=r.url,cookies=self.cj)
			t=r.text
		t="".join(t.split())
		t=t.replace('\\','')
		rst=re.findall('action-data="uid=(.*?)&fnick=(.*?)&f=(.*?)&refer_flag=(.*?)&refer_lflag=(.*?)"',t)
		form={'uid':'','objectid':'','f':'1','extra':'','refer_sort':'','refer_flag':'','location':'','oid':'','wforce':'1','nogroup':'false','fnick':'','refer_lflag':'',
		}
		if rst:
			form['uid']=rst[0][0]
			form['oid']=rst[0][0]
			form['fnick']=rst[0][1]
			form['f']=rst[0][2]
			form['refer_flag']=rst[0][3]
			form['refer_lflag']=rst[0][4]
		rst=re.findall("page_\d{6}_home",t)
		if rst:
			form['location']=rst[0]
		return form

	def follow(self,u):
		followUrl='http://weibo.com/aj/f/followed?ajwvr=6&__rnd='+str(int(time.time()*1000))
		form=self.getForm(u)
		form['_t']='0'
		post_data=urllib.parse.urlencode(form).encode(encoding='utf-8')
		rst=urllib.request.Request(url=followUrl,data=post_data,headers=self.headers)
		rst.add_header('Referer',u)
		rsp=urllib.request.urlopen(rst).read()
		try:
			rsp=rsp.decode('utf-8')
		except:
			pass
		rst=re.findall('"code":"(\d*)"',str(rsp))
		if rst and rst[0]=='100000':
			print(form['fnick'],'follow successfully!')
			return True
		print(form['fnick'],'follow fail!')
		return False

	def unfollow(self,u):
		unfollowUrl='http://weibo.com/aj/f/unfollow?ajwvr=6'
		form=self.getForm(u)
		post_data=urllib.parse.urlencode(form).encode(encoding='utf-8')
		rst=urllib.request.Request(url=unfollowUrl,data=post_data,headers=self.headers)
		rst.add_header('Referer',u)
		rsp=urllib.request.urlopen(rst).read()
		rst=re.findall('"code":"(\d*)"',str(rsp))
		if rst and rst[0]=='100000':
			print(form['fnick'],'unfollow successfully!')
			return True
		print(form['fnick'],'unfollow fail!')
		return False

	def getFollow(self,p):
		u='http://weibo.com/p/1005053803719362/myfollow?t=1&pids=Pl_Official_RelationMyfollow__110&cfs=&Pl_Official_RelationMyfollow__110_page='+str(p)+'&ajaxpagelet=1&ajaxpagelet_v6=1&__ref=/p/1005053803719362/myfollow&_t=FM_145917238057569'
		rst=urllib.request.Request(url=u,headers=self.headers)
		rsp=urllib.request.urlopen(rst).read()
		try:
			rsp=rsp.decode('utf-8')
		except:
			rsp=rsp.decode('gbk')
		s="".join(rsp.split())
		s=s.replace('\\','')
		url=re.findall('screen_name"href="(.*?from=myfollow_all)',s)
		nick=re.findall('&screen_name=(.*?)&',s)
		for i in range(len(url)):
			url[i]='http://weibo.com'+url[i]
		rt=[]
		date=int(time.time())
		for i in range(len(url)):
			d={'url':url[i],'nick':nick[i],'date':date,'follow':1}
			rt.append(d)
		return rt

def setFollowListToMongo():
	import pymongo
	c='D:\\workspace\\python\\SinaWeibo\\config\\cookie'
	fl=follow(c)
	p=1
	while True:
		coll=fl.getFollow(p)
		p=p+1
		if len(coll)==0:
			break
		client = pymongo.MongoClient(host='localhost', port=27017)
		db = client['weibo']
		cl=db['follow']
		cl.insert(coll)
		print('insert',len(coll),' follow')


def get_db():
	client = pymongo.MongoClient(host='localhost', port=27017)
	db = client['weibo']
	return db
def testFollow():
	f=follow('D:\\workspace\\python\\SinaWeibo\\config\\cookie')
	f.follow('http://weibo.com/n/%E6%96%87%E9%83%BD-%E6%B1%A4%E5%AE%B6%E5%87%A4?refer_flag=1001030001_')
def testUnfollow():
	f=follow('D:\\workspace\\python\\SinaWeibo\\config\\cookie')
	f.unfollow('http://weibo.com/u/1742566624?refer_flag=1001030103_')
def testGetForm():
	f=follow('D:\\workspace\\python\\SinaWeibo\\config\\cookie')
	print(f.getForm('http://weibo.com/u/3404872632?from=myfollow_all'))
if __name__=='__main__':
	#setFollowListToMongo()
	testUnfollow()

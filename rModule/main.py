# -*- coding: utf-8 -*-
# @Date    	: 2016-03-25 16:32:42
# @Author  	: mr0cheng
# @email	: c15271843451@gmail.com

'''
Sub module main.py file achieve retweet function.
'''

import os,sys,time,re,random
import pymongo

__file__ = os.path.abspath(__file__)
if os.path.islink(__file__):
	__file__ = getattr(os, 'readlink', lambda x: x)(__file__)

current_path = os.path.dirname(os.path.abspath(__file__))
sys.path.append(current_path)
from search import search
from retweet import retweet

log	=os.path.join(current_path,'log')

'''
params:
	t 	:Keyword search
	p 	:the page num
	c 	:cookie file
'''
def main(c,t='转发抽奖',p=2):
	sh 	=search(c)
	lt 	=sh.search(t,p)
	setWeiboMongo(lt)
	rst=getOneWeibo()
	if rst is False:
		print('No more weibo to retweet!')
		return False
	rt=retweet(c)
	state=rt.retweet(rst['mid'],rst['reason'])
	if state:
		return rst
	return False

def get_db():
	client = pymongo.MongoClient(host='localhost', port=27017)
	db = client['weibo']
	return db

def getOneWeibo():
	reason=['希望是我','谢谢','如果我能中就好了','快点抽吧','我都等不及了','好想要啊','可以中一次吗','试试手气','随手转发','不要骗我哦']
	db=get_db()
	cl=db['retweet']
	rst=cl.find({'retweet':0}).sort("mid", pymongo.ASCENDING)
	for rt in rst:
		cl.update({'_id':rt['_id']},{'$set':{'retweet':1}})
		print('update',rt['mid'],' retweet=1')
		if len(rt['url'])>4:
			print(rt['mid'],' too many users to follow,find another weibo')
			continue
		rt['reason']=reason[random.randint(0,len(reason)-1)]
		if rt['friend']>0:
			cl=db['follow']
			rst=cl.find({'follow':1})
			rint=random.randint(0,rst.count()-rt['friend'])
			for i in range(rint,rint+rt['friend']):
				rt['reason']=rt['reason']+'@'+rst[i]['nick']+' '
		return rt
	return False

def setWeiboMongo(rst):
	db=get_db()
	cl=db['retweet']
	try:
		maxMid=cl.find().sort("mid", pymongo.DESCENDING)[0]['mid']
	except:
		maxMid='0'
	coll=[]
	for c in rst:
		dt={}
		cm=re.findall('comment_txt.*?/p',c)[0]
		dt['mid']=returnMid(c)
		if dt['mid']<=maxMid:
			break
		dt['url']=returnUrl(c)
		dt['friend']=returnFri(cm)
		dt['retweet']=0
		coll.append(dt)
	if coll:
		cid=cl.insert(coll)
	print('insert',len(coll),' retweet document!')
	return coll

def returnMid(c):
	return re.findall('\d{16}',c)[0]

def returnUrl(c):
	r=[]
	nick,url=re.findall('W_textaW_fb"nick-name="(.*?)"href="(.*?)"target',c)[0]
	r.append({'link':url,'nick':nick})
	cm=re.findall('comment_txt.*?/p',c)[0]
	if re.findall('关注',cm):
		tr=[]
		url=[]
		nick=[]
		rst=re.findall('ahref="(http.*?)"usercard="name=(.*?)[&|"]',cm)
		for i in rst:
			url.append(i[0])
			nick.append(i[1])
		for i in range(len(url)):
			d={}
			lt=re.findall('抽奖|好友',url[i])
			if len(lt)==0:
				d['link']=url[i]
				d['nick']=nick[i]
				tr.append(d)
		
		for i in tr:
			flag=False
			for j in r:
				if i['nick']==j['nick']:
					flag=True
					break
			if not flag:
				r.append(i)
	return r

def returnFri(cm):
	d=0
	c={
		'一':1,'1':1,'二':2,'2':2,'三':3,'3':3,'四':4,'4':4,'五':5,'5':5,'六':6,'6':6
	}
	s=re.findall('(.{1})[位|个].{0,4}好友',cm)
	if s:
		try:
			d=c[s[0]]
		except:
			pass
	return d

if __name__=='__main__':
	c='D:\\workspace\\python\\SinaWeibo\\config\\cookie'
	t='转发抽奖'
	p=2
	sh 	=search(c)
	rst 	=sh.search(t,p)
	setWeiboList(rst)
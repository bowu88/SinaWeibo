'''
Sub module main.py file achieve login function.
'''

import os,sys,time
import pymongo

__file__ = os.path.abspath(__file__)
if os.path.islink(__file__):
    __file__ = getattr(os, 'readlink', lambda x: x)(__file__)

current_path = os.path.dirname(os.path.abspath(__file__))
sys.path.append(current_path)
log	=os.path.join(current_path,'log')
from follow import follow
def get_db():
	client = pymongo.MongoClient(host='localhost', port=27017)
	db = client['weibo']
	return db

def main(c,r):
	if r:
		uf(c)
		f(c,r['url'])

def f(c,url):
	db=get_db()
	cl=db['follow']
	coll=[]
	fl=follow(c)
	date=returnDate()
	for i in url:
		rst=cl.find({'nick':i['nick']})
		if rst.count()==0:
			if fl.follow(i['link']):
				coll.append({'url':i['link'],'date':date,'nick':i['nick'],'follow':1})
		elif rst[0]['follow']==0:
			if fl.follow(i['link']):
				cl.update({'_id':rst[0]['_id']},{'$set':{'follow':1,'date':date}})
		print('update',i['nick'],'follow=1,date=',date)
	
	if len(coll)>0:
		db['follow'].insert(coll)
	print('insert',len(coll),' follow document!')
def returnDate():
	return int(time.time())+86400*5
'''
unfollow one by my follow list
'''
def uf(c):
	db=get_db()
	cl=db['follow']
	rst=cl.find({'follow':1}).sort('date',pymongo.ASCENDING)
	for i in rst:
		fl=follow(c)
		if fl.unfollow(i['url']):
			cl.update({'_id':i['_id']},{'$set':{'follow':0}})
			print('update',i['nick'],'follow=0')
		break


# -*- coding:utf-8 -*-
from urllib import request,parse
import urllib
import http.cookiejar
import re,json
import rsa,binascii,base64
'''
params:
	url_0 	:To test whether need to log in again
	url_1 	:Nothing to do
	url_2 	:preLogin for got unknown params
	url_3 	:login
'''
class login(object):
	url_0	='http://weibo.com/u/3803719362/home?wvr=5'
	url_1	='http://weibo.com/login.php'
	url_2	='http://login.sina.com.cn/sso/prelogin.php?%s'
	url_3	='http://login.sina.com.cn/sso/login.php?client=ssologin.js(v1.4.18)'
	code_url	='http://login.sina.com.cn/cgi/pin.php?r=96483122&s=0&p=gz-fcec6863b75031dcd603688e587baa78ffdf'

	pcid='gz-fcec6863b75031dcd603688e587baa78ffdf'
	servertime=''
	nonce=''
	rsakv=''
	pubKey=''
	su=''
	headers={
			'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:44.0) Gecko/20100101 Firefox/44.0',
		}
	def __init__(self,u,p,c):
		self.cj=http.cookiejar.LWPCookieJar(c)
		self.cookie_support=urllib.request.HTTPCookieProcessor(self.cj)
		self.opener=urllib.request.build_opener(self.cookie_support,urllib.request.HTTPHandler)
		urllib.request.install_opener(self.opener)
		self.u=u
		self.p=p
	def getSP(self):
	    n=self.pubKey
	    puk = rsa.PublicKey(int(
	            n,16), 65537) 
	    #ct=ciphertext
	    ct=(str(self.servertime)+'\t'+str(self.nonce)+'\n'+str(self.p)).encode()
	    return binascii.b2a_hex(rsa.encrypt(ct, puk)).decode()

	def tryLogin(self):
		form={
			'entry':'weibo',
			'gateway':'1',
			'from':'',
			'savestate':'7',
			'useticket':'1',
			'pagerefer':'http://passport.weibo.com/visitor/visitor?entry=miniblog&a=enter&url=http%3A%2F%2Fweibo.com%2F&domain=.weibo.com&sudaref=http%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3DkGDeb4dJkAWFRYB2DlGO69HMSLdFm4k6l7yGXAaQ5h3%26wd%3D%26eqid%3Da7d36c3a000bd62f0000000456bd40ce&ua=php-sso_sdk_client-0.6.14&_rand=1455243527.5495',
			'vsnf':'1',
			'su':self.su,
			'service':'miniblog',
			'servertime':self.servertime,
			'nonce':self.nonce,
			'pwencode':'rsa2',
			'rsakv':self.rsakv,
			'sp':self.getSP(),
			'sr':'1366*768',
			'encoding':'UTF-8',
			'prelt':'101',
			'url':'http://weibo.com/ajaxlogin.php?framelogin=1&callback=parent.sinaSSOController.feedBackUrlCallBack',
			'returntype':'META',      
		}
		post_data=urllib.parse.urlencode(form).encode(encoding='utf-8')
		rst=urllib.request.Request(url=self.url_3,data=post_data,headers=self.headers)
		rsp=str(urllib.request.urlopen(rst).read())
		r=re.findall('retcode=(\d{1,5}?)',rsp)
		if r:
			if r[0]=='0':
				r=re.findall('http://pass.*retcode=0',str(rsp))[0]
				rst=urllib.request.Request(url=r,headers=self.headers)
				urllib.request.urlopen(rst)
			elif r[0]=='4039':
				f=open('code.jpg','wb')
				f.write(urllib.request.urlopen(url=self.code_url).read())
				f.close()
				door=input('please input verify code:')
				form['door']=door
				form['pcid']=self.pcid
				post_data=urllib.parse.urlencode(form).encode(encoding='utf-8')
				rst=urllib.request.Request(url=self.url_3,data=post_data,headers=self.headers)
				rsp=urllib.request.urlopen(rst).read()
				r=re.findall('retcode=(\d{1,5}?)',str(rsp))
				if r[0]=='0':
					r=re.findall('http://pass.*retcode=0',str(rsp))[0]
					rst=urllib.request.Request(url=r,headers=self.headers)
					urllib.request.urlopen(rst)
				else:
					print('sorry,i have try,but...')
					return False
			else:
				print('sina weibo unkown error??')
				return False
		else:
			return False
		print('sina weibo login sucessfully!')
		return True
		
	#PK==pubKey 
	def getPK(self):
		params={
			'entry':'weibo',
			'callback':'sinaSSOController.preloginCallBack',
			'su':self.su,
			'rsakt':'mod',
			'checkpin':'1',
			'client':'ssologin.js(v1.4.18)',
			'_':'1455151422604'
		}
		self.url_2=self.url_2%urllib.parse.urlencode(params)
		rst=urllib.request.Request(url=self.url_2,headers=self.headers)
		rsp=urllib.request.urlopen(rst).read()
		try:
			rsp=rsp.decode('utf-8')
		except:
			rsp=rsp.decode('gbk')
		j=json.loads(re.findall('{.*}', rsp)[0])
		self.rsakv=j['rsakv']
		self.nonce=j['nonce']
		self.pubKey=j['pubkey']
		self.servertime=j['servertime']
        
	def isLoginAgain(self):
		try:
			self.cj.load(ignore_discard=True, ignore_expires=True)
		except:
			return True
		rst=urllib.request.Request(url=self.url_0,headers=self.headers)
		rsp=urllib.request.urlopen(rst).read()
		try:
			rsp=rsp.decode('utf-8')
		except:
			rsp=rsp.decode('gbk')
		print(rsp)
		rst=re.findall('我的首页',rsp)
		if rst:
			print('Luckily,dont need login again!')
			return False
		print('Cookie has been over expired,login again!')
		return True

	def login(self):
		if self.isLoginAgain() is False:
			return True
		self.su=str(base64.encodestring(bytes(self.u,encoding='utf-8'))[:-1],encoding='utf-8')
		self.getPK()
		state=self.tryLogin()
		self.cj.save(ignore_discard=True, ignore_expires=True)
		return state

if __name__=='__main__':
	c='D:\\workspace\\python\\SinaWeibo\\config\\cookie'
	lg=login('','',c)
	lg.login()
    
# SinaWeibo
自动转发带`转发抽奖`字样的微博，参与抽奖活动。


## 模块列表(具体内容请点击相应的模块)
* [lModule](https://github.com/chengshuyi/SinaWeibo/blob/master/lModule/README.md):登录模块  
* [rModule](https://github.com/chengshuyi/SinaWeibo/blob/master/rModule/README.md):转发模块  
* [fModule](https://github.com/chengshuyi/SinaWeibo/blob/master/fModule/README.md):关注模块  

## 环境配置
* python version 3.5  
* python extra library:  
	- requests  
	- rsa  
	- binascii  
	- base64  
	- pymongo  
	- json  
* mongodb  

## 使用方法
```python
u=''		#modify to your username(phone number,email)
p='' 		#modify to your password
```

##mongodb数据库`weibo`
* follow collection  
	- {'url':'http://weibo.com/n/%E6%96%87%E9%83%BD-%E6%B1%A4%E5%AE%B6%E5%87%A4?refer_flag=1001030001_','date':'unix time stamp','nick':'name','follow':1}  
	- {'url':'http://weibo.com/u/3404872632?from=myfollow_all','date':'unix time stamp','nick':'name','follow':1}  
	- 2种url格式,第一种是属于从微博信息中提取的url,仍未关注。第二种是从主页已关注列表获取的url。  
* retweet collection  
	- {'mid':'3958445813689070','url':[{'link':'http://weibo.com/n/%E4%B9%90%E8%AF%8D%E8%83%8C%E5%8D%95%E8%AF%8D?refer_flag=1001030001_','nick':'name'},{'link':'http://weibo.com/n/%E6%96%87%E9%83%BD-%E6%B1%A4%E5%AE%B6%E5%87%A4?refer_flag=1001030001_','nick':'name'],'friend':'3','retweet':0}  
	- 在retweet之后，将url和date插入follow collection  


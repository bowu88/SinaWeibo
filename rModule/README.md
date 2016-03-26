# rModule:转发的模块,目前需要拥有的功能
* retweet转发一条微博
* search微博搜索功能的接口


### main.py文件
* 每一个模块必须有的入口文件  
* 需要传递进去参数  
* 需要返回的参数

### retweet.py文件
* 传入mid,reason,cookie
* 需要返回是否转发成功
```python
rt=retweet(rst['mid'],rst['reason'],c)
state,rsp=rt.retweet() 	#rsp is json format
```

### search.py文件(你可以修改名字)
* 传入参数t,p,c
* 需要返回整个html
```python
sh 	=search(t,p,c)
state,js 	=sh.search() 	#js is html doc
```


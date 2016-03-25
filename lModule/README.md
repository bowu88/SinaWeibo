# lModule:登录模块,目前需要拥有的功能
* login登录,并检测cookie是否可用

### main.py文件
* 每一个模块必须有的入口文件  
* 需要传递进去参数  
* 需要返回的参数

```python
params:
	u 	:username
	p 	:password
	c 	:the path of cookie

return:
	state	:login successfully?
```

### login.py文件
* init传进参数
* login类唯一调用函数login()

```python
c='D:\\workspace\\python\\SinaWeibo\\config\\cookie'
lg=login('your name','your password',c)
lg.login()
```

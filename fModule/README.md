# fModule 关注模块，目前具有的功能
* follow.py实现关注和取消关注

## follow.py使用方法
```python
fl=follow(c) 	#c是cookie文件
fl.follow(url) 	#被关注者的url-->访问url-->getForm()-->follow

fl.unfollow(url) 	#被关注者的url-->访问url-->getForm()-->unfollow
```
* follow 返回bool类型  
* unfollow 返回bool类型  
* getFollow 返回已关注列表  

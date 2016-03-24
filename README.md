# SinaWeibo
自动转发带`转发抽奖`字样的微博，参与抽奖活动。


## 模块列表(具体内容请点击相应的模块)
* [lModule](https://github.com/chengshuyi/SinaWeibo/blob/master/lModule/README.md):登录模块  
* [rModule](https://github.com/chengshuyi/SinaWeibo/blob/master/rModule/README.md):转发模块  
* [fModule](https://github.com/chengshuyi/SinaWeibo/blob/master/fModule/README.md):关注模块  

## 每一个模块的要求
* 必须要有一个log文件,记录操作的关键内容(方便日后的debug)  
* main.py调用每一个模块,由main.py完成模块之间的交互作用  
* 每一个模块要有main.py文件,用于与主目录main.py的交互

# Sortng Hat 分院帽

### Overview
霍格沃茨微信群管理机器人

### Framework
[wxpy: 用 Python 玩微信](https://github.com/youfou/wxpy)

### How it works
1. 抓取Forest请求，获取以下接口:
	1. 登录
	2. 添加Forest关注
	3. 查询关注账户专注时间
		1. by day
		2. by month
  
2. 基于wxpy为上述功能添加微信群关键词监听
	1. 查询学院人数, 依据人数计算学院分权重
	2. 查询学院分，依据各学院成员专注时间与人数权重计算学院分，当月清算
	3. 添加Forest关注

# -*- coding: utf-8 -*-
# @Author: JinZhang
# @Date:   2019-03-15 10:50:51
# @Last Modified by:   JinZhang
# @Last Modified time: 2019-03-15 11:09:13
import redis;

from _Global import _GG;

class RedisDB(object):
	"""docstring for RedisDB"""
	def __init__(self):
		super(RedisDB, self).__init__();
		srvConf = _GG("ServerConfig").Config(); # 服务配置
		self.__pool = redis.ConnectionPool(host = srvConf.Get("redis", "host"), port = int(srvConf.Get("redis", "port")), decode_responses=True);

	def __call__(self):
		return redis.Redis(connection_pool = self.__pool);
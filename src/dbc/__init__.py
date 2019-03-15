# -*- coding: utf-8 -*-
# @Author: JinZhang
# @Date:   2019-03-12 15:04:31
# @Last Modified by:   JinZhang
# @Last Modified time: 2019-03-15 11:02:10

from MySQLDB import MySQLDB;
from RedisDB import RedisDB;

class DBCManager(object):
	"""docstring for DBCManager"""
	def __init__(self):
		super(DBCManager, self).__init__();

	def MySQL(self):
		if not hasattr(self, "__mysql"):
			self.__mysql = MySQLDB();
		return self.__mysql;

	def RedisDB(self):
		if not hasattr(self, "__redis"):
			self.__redis = RedisDB();
		return self.__redis;
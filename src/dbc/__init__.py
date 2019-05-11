# -*- coding: utf-8 -*-
# @Author: JinZhang
# @Date:   2019-03-12 15:04:31
# @Last Modified by:   JinZhang
# @Last Modified time: 2019-05-09 19:19:40
import os;
import sys;

CURRENT_PATH = os.path.dirname(os.path.realpath(__file__));
sys.path.append(CURRENT_PATH);

__all__ = ["DBCManager"];

try:
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

		def Redis(self):
			if not hasattr(self, "__redis"):
				self.__redis = RedisDB();
			return self.__redis();
except Exception as e:
	raise e;
finally:
	sys.path.remove(CURRENT_PATH);
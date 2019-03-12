# -*- coding: utf-8 -*-
# @Author: JimDreamHeart
# @Date:   2019-02-24 17:25:31
# @Last Modified by:   JimZhang
# @Last Modified time: 2019-03-02 00:28:31
import pymysql;

from _Global import _GG;

class DBCManager(object):
	"""docstring for DBCManager"""
	def __init__(self):
		super(DBCManager, self).__init__()
	
	def getConnection(self):
		SrvConf = _GG("ServerConfig").Config(); # 服务配置
		return pymysql.connect(host = SrvConf.Get("database", "host"),
			port = int(SrvConf.Get("database", "port")),
			user = SrvConf.Get("database", "user"),
			password = SrvConf.Get("database", "password"),
			database = SrvConf.Get("database", "database"),
			charset = "utf8");

	def execute(self, sql):
		ret, results = False, [];
		conn = self.getConnection();
		cursor = conn.cursor(cursor=pymysql.cursors.DictCursor);
		try:
			cursor.execute(sql);
			if sql.split(" ")[0].lower() == "select":
				results = cursor.fetchall();
				ret = len(results) > 0;
			else:
				conn.commit();
				ret = True;
		except Exception as e:
			print(e);
			conn.rollback();
		finally:
			cursor.close();
			conn.close();
		return ret, results;

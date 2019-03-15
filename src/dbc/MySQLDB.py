# -*- coding: utf-8 -*-
# @Author: JinZhang
# @Date:   2019-03-15 10:58:21
# @Last Modified by:   JinZhang
# @Last Modified time: 2019-03-15 19:36:52
import pymysql;

from _Global import _GG;

class MySQLDB(object):
	"""docstring for MySQLDB"""
	def __init__(self):
		super(MySQLDB, self).__init__();

	def getConnection(self):
		srvConf = _GG("ServerConfig").Config(); # 服务配置
		return pymysql.connect(host = srvConf.Get("mysql", "host"),
			port = int(srvConf.Get("mysql", "port")),
			user = srvConf.Get("mysql", "user"),
			password = srvConf.Get("mysql", "password"),
			database = srvConf.Get("mysql", "database"),
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
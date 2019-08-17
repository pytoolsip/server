# -*- coding: utf-8 -*-
# @Author: JimZhang
# @Date:   2019-02-24 05:05:50
# @Last Modified by:   JinZhang
# @Last Modified time: 2019-03-15 11:06:02
import os;
import sys;
import time;
import grpc;
from concurrent import futures; #具有线程池和进程池、管理并行编程任务，处理非确定性的执行流程、进程/线程同步等功能
# 当前文件位置
CURRENT_PATH = os.path.dirname(os.path.realpath(__file__));
# 添加搜索路径
if os.path.join(CURRENT_PATH, "core") not in sys.path:
	sys.path.append(os.path.join(CURRENT_PATH, "core"));

# 加载工程
import _Global as _G;
from function.base import *;
from net.proto import common_pb2_grpc;
from dbc import DBCManager;

from behaviorCore.BaseBehavior import BaseBehavior;
from behaviorCore.BehaviorManager import BehaviorManager;
from logCore.Logger import Logger;
import rsaCore;

from config.ServerConfig import ServerConfig;

class Loader(object):
	def __init__(self, mainPath):
		super(Loader, self).__init__();
		_G.initGlobal_GTo_Global(); # 初始化全局变量
		pass;

	def loadMainServer(self):
		srvConf = _G._GG("ServerConfig").Config(); # 服务配置
		grpcServer = grpc.server(futures.ThreadPoolExecutor(max_workers = int(srvConf.Get("server", "max_workers")))); # 最多有多少work并行执行任务
		commonServer = require(CURRENT_PATH, "server", "CommonServer")(); # 获取服务器对象
		common_pb2_grpc.add_CommonServicer_to_server(commonServer, grpcServer); # 添加函数方法和服务器，服务器端会进行反序列化。
		print(":".join([srvConf.Get("server", "host"), srvConf.Get("server", "port")]));
		grpcServer.add_insecure_port(":".join([srvConf.Get("server", "host"), srvConf.Get("server", "port")])); # 建立服务器和端口
		# 设置注册及注销方法
		grpcServer.registerMethod = commonServer.registerMethod;
		grpcServer.unregisterMethod = commonServer.unregisterMethod;
		# 设置服务器对象到全局
		_G.setGlobalVarTo_Global("MainServer", grpcServer);
		return grpcServer;

	def registerSrvMethod(self):
		# 扩展服务器方法
		require(CURRENT_PATH, "server", "ExtendSrvMethod")();

	def loadLogger(self):
		srvConf = _G._GG("ServerConfig").Config(); # 服务配置
		path = srvConf.Get("log", "path", "").replace("\\", "/");
		if len(path) > 0 and path[-1] != "/":
			path += "/";
		name = srvConf.Get("log", "name", "PyToolsIP");
		curTimeStr = time.strftime("%Y_%m_%d", time.localtime());
		logger = Logger("Common", isLogFile = True, logFileName = "".join([_G._GG("g_ProjectPath"), path, name, "_%s.log"%curTimeStr]),
			maxBytes = int(srvConf.Get("log", "maxBytes")), backupCount = int(srvConf.Get("log", "backupCount")));
		_G.setGlobalVarTo_Global("Log", logger); # 设置日志类的全局变量
		return logger;

	def lockGlobal_G(self):
		_G.lockGlobal_GTo_Global(); # 锁定全局变量

	def loadGlobalInfo(self):
		self.loadPaths(); # 加载全局路径名变量
		self.loadObjects(); # 加载全局对象变量
		self.loadConfigs(); # 加载全局配置变量
		self.loadResources(); # 加载全局资源变量
		pass;

	# 加载全局路径名变量
	def loadPaths(self):
		_G.setGlobalVarTo_Global("g_ProjectPath", os.path.abspath(os.path.join(CURRENT_PATH, "..")) + "/");
		_G.setGlobalVarTo_Global("g_BinPath", _G._GG("g_ProjectPath") + "bin/");
		_G.setGlobalVarTo_Global("g_LibPath", _G._GG("g_ProjectPath") + "lib/");
		_G.setGlobalVarTo_Global("g_SrcPath", CURRENT_PATH + "/");
		pass;

	# 加载全局对象变量
	def loadObjects(self):
		_G.setGlobalVarTo_Global("BaseBehavior", BaseBehavior); # 设置组件基础类变量（未实例化）
		_G.setGlobalVarTo_Global("BehaviorManager", BehaviorManager()); # 设置组件管理器的全局变量
		_G.setGlobalVarTo_Global("DBCManager", DBCManager()); # 设置数据库连接管理器的全局变量
		pass;

	def loadFuncs(self):
		# 加载rsa密钥解码方法
		_G.setGlobalVarTo_Global("DecodeStr", rsaCore.decodeStr);
		_G.setGlobalVarTo_Global("g_PublicKey", rsaCore.getPublicKey);

	# 加载全局配置变量
	def loadConfigs(self):
		print("Loading configs......");
		_G.setGlobalVarTo_Global("ServerConfig", ServerConfig()); # 设置服务配置的全局变量
		print("Loaded configs!");
		pass;

	# 加载全局资源变量
	def loadResources(self):
		print("Loading resources......");
		print("Loaded resources!");
		pass;
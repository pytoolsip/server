# -*- coding: utf-8 -*-
# @Author: JimZhang
# @Date:   2019-02-23 12:36:46
# @Last Modified by:   JimDreamHeart
# @Last Modified time: 2019-03-12 23:27:39
import os,time,json;

# 安装依赖模块
dependJson = os.path.abspath(os.path.join(os.path.dirname(__file__),"../depend.json"));
if os.path.exists(dependJson):
	with open(dependJson, "r") as f:
		dependList = json.loads(f.read());
		for depend in dependList:
			if os.system("pip show " + depend) != 0:
				os.system("pip install " + depend);

# 加载工程
from _load import Loader;
Loader = Loader(os.getcwd()); # 获取加载器
Loader.loadGlobalInfo(); # 加载全局变量
MainServer = Loader.loadMainServer(); # 加载主服务
Log = Loader.loadLogger(); # 加载日志
Loader.lockGlobal_G(); # 锁定全局变量

# 启动主服务
if __name__ == '__main__':
	# 启动服务器
	MainServer.start();
	# 注册服务方法
	Loader.registerSrvMethod();
	Log.i("Start server successful！");
	while True:
		time.sleep(10*60);
		break;
	MainServer.stop(0);
	Log.i("Stop server successful！");
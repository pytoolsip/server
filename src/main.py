# -*- coding: utf-8 -*-
# @Author: JimZhang
# @Date:   2019-02-23 12:36:46
# @Last Modified by:   JinZhang
# @Last Modified time: 2019-05-09 19:15:02
import sys,os,time;

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
		time.sleep(365*24*60*60); # 1年时长
		break;
	MainServer.stop(0);
	Log.i("Stop server successful！");
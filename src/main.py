# -*- coding: utf-8 -*-
# @Author: JimZhang
# @Date:   2019-02-23 12:36:46
# @Last Modified by:   JimDreamHeart
# @Last Modified time: 2019-03-06 00:06:40
import os,time;

from _load import Loader;
from _Global import _GG;

# 加载全局变量
Loader = Loader(os.getcwd());
Loader.loadGlobalInfo();
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
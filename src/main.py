# -*- coding: utf-8 -*-
# @Author: JimZhang
# @Date:   2019-02-23 12:36:46
# @Last Modified by:   JinZhang
# @Last Modified time: 2019-03-13 20:38:42
import sys,os,time;
# 设置默认编码格式
reload(sys);
sys.setdefaultencoding('utf8');

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
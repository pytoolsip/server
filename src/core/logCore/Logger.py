# -*- coding: utf-8 -*-
# @Author: JimDreamHeart
# @Date:   2019-03-03 22:54:01
# @Last Modified by:   JimDreamHeart
# @Last Modified time: 2019-03-12 23:44:27
import os,logging;
from logging.handlers import RotatingFileHandler;

from _Global import _GG;

LevelKeyMap = {
	"debug" : logging.DEBUG,
	"info" : logging.INFO,
	"warning" : logging.WARNING,
	"error" : logging.ERROR,
};

MethodKeyMap = {
	"d" : "debug",
	"i" : "info",
	"w" : "warning",
	"e" : "error",
};

# LogRecord类
class LogRecord(logging.LogRecord):
	"""docstring for LogRecord"""
	def __init__(self, name, level, pathname, lineno, msg, args, exc_info, func=None):
		pathname = pathname.replace(_GG("g_SrcPath"), ""); # 修改路径为相对路径
		super(LogRecord, self).__init__(name, level, pathname, lineno, msg, args, exc_info, func=None);

	def getMessage(self):
		logMsg = "{} "*(len(self.args) + 1);
		return logMsg.format(self.msg, *self.args);

# 重置logging的LogRecord类
logging.LogRecord = LogRecord;

# Logger类
class Logger(logging.Logger):
	"""docstring for Logger"""
	def __init__(self, name, level = "debug", fmt="%(asctime)s - %(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s",
		methodKeyMap = None, isLogStream = True, isLogFile = False, logFileName = "", maxBytes = 1000, backupCount = 10):
		super(Logger, self).__init__(name, level = LevelKeyMap[level]);
		self.__formatter = logging.Formatter(fmt);
		self.setLevel(LevelKeyMap[level]);
		# 设置handler
		if isLogStream:
			self.__setStreamHandler__(level = level);
		if isLogFile:
			if len(logFileName) == 0:
				logFileName = name;
			self.__setFileHandler__(logFileName, maxBytes, backupCount, level = level);
		# 新增日志打印方法接口
		self.__initMethods__(methodKeyMap);

	def __addHandler__(self, handler, level = "debug"):
		handler.setLevel(LevelKeyMap[level]);
		handler.setFormatter(self.__formatter);
		self.addHandler(handler);

	# 设置日志窗口输出
	def __setStreamHandler__(self, level = "debug"):
		if not hasattr(self, "__streamHandler"):
			self.__streamHandler = logging.StreamHandler();
			self.__addHandler__(self.__streamHandler, level = level);

	# 设置日志文件输出
	def __setFileHandler__(self, fileName, maxBytes, backupCount, level = "debug"):
		if not hasattr(self, "__fileHandler"):
			dirName = os.path.abspath(os.path.dirname(fileName));
			if not os.path.exists(dirName):
				os.mkdir(dirName);
			self.__fileHandler = RotatingFileHandler(fileName, maxBytes = maxBytes, backupCount = backupCount, encoding = "utf-8");
			self.__addHandler__(self.__fileHandler, level = level);

	# 初始化方法
	def __initMethods__(self, methodKeyMap = None):
		if methodKeyMap == None:
			methodKeyMap = MethodKeyMap;
		for key in methodKeyMap:
			setattr(self, key, self.__getMethod__(methodKeyMap[key]));

	def __getMethod__(self, level):
		def method(msg, *args, **kwargs):
			if self.isEnabledFor(LevelKeyMap[level]):
				self._log(LevelKeyMap[level], msg, args, **kwargs);
		return method;


# -*- coding: utf-8 -*-
# @Author: JimDreamHeart
# @Date:   2019-02-23 21:07:59
# @Last Modified by:   JimDreamHeart
# @Last Modified time: 2019-04-06 10:59:48
import os,json,time;
import hashlib;

from _Global import _GG;
from net.proto import common_pb2,common_pb2_grpc;

class CommonServer(common_pb2_grpc.CommonServicer):
	"""docstring for CommonServer"""
	def __init__(self):
		super(CommonServer, self).__init__();
		self.__methodDict = {};

	def registerMethod(self, methodName, method):
		if callable(method):
			self.__methodDict[methodName] = method;

	def unregisterMethod(self, methodName):
		if methodName in self.__methodDict:
			self.__methodDict.pop(methodName);

	def Request(self, request, context):
		retDate = {"isSuccess" : False};
		methodName = request.key;
		if methodName in self.__methodDict:
			isSuccess, data = self.__methodDict[methodName](json.loads(bytes.decode(request.data)), context);
			retDate = {
				"isSuccess" : bool(isSuccess),
				"data" : str.encode(json.dumps(data)),
			};
		return common_pb2.Resp(**retDate);

	def _splitVersion_(self, version):
		return [int(ver) for ver in version.replace(" ", "").split(".") if ver.isdigit()];

	def _getFileName_(self, key = "", name = "", category = "", version = "", suffix = ""):
		if not key:
			if category:
				name = self.__verifyCategory__(category) + name;
			key = hashlib.md5(name.encode("utf-8")).hexdigest();
		if version:
			version = "_" + version;
		if suffix and suffix[0] != ".":
			suffix = "." + suffix;
		return "".join([key, version, suffix]);

	def __verifyCategory__(self, category):
		category = category.replace(" ", "");
		if len(category) > 0 and category[-1] != "/":
			category += "/";
		return category;
	
	def Login(self, request, context):
		sql = "SELECT * FROM user WHERE name = '%s' AND password = '%s'"%(request.name, request.password);
		ret, results = _GG("DBCManager").MySQL().execute(sql);
		if ret:
			userInfo = results[0];
			return common_pb2.LoginResp(isSuccess = True, 
				userInfo = common_pb2.UserInfo(uid = userInfo["id"], name = userInfo["name"], email = userInfo["email"]));
		return common_pb2.LoginResp(isSuccess = False);

	def Register(self, request, context):
		# 校验验证码
		if _GG("DBCManager").Redis().hexists("verification_code", request.email) and _GG("DBCManager").Redis().hget("verification_code", request.email) == request.veriCode:
			# 校验提交的信息中是否已存在于数据库中
			sql = "SELECT id FROM user WHERE name = '%s'"%request.name;
			ret, results = _GG("DBCManager").MySQL().execute(sql);
			if ret:
				return common_pb2.Resp(isSuccess = False);
			# 插入注册数据到数据库中
			sql = "INSERT INTO user(name, password, email) VALUES('%s', '%s', '%s')"%(request.name, request.password, request.email);
			ret, results = _GG("DBCManager").MySQL().execute(sql);
			return common_pb2.Resp(isSuccess = ret);
		return common_pb2.Resp(isSuccess = False, data = str.encode(json.dumps({"content" : "验证码错误，请重新发送并输入！"})));

	def Upload(self, request, context):
		# 校验所传用户ID数据
		sql = "SELECT name FROM user WHERE id = '%d'"%request.uid;
		ret, results = _GG("DBCManager").MySQL().execute(sql);
		if not ret:
			return common_pb2.Resp(isSuccess = False);
		# 判断请求信息是否正确
		toolVerList = self._splitVersion_(request.version);
		if len(toolVerList) != 3:
			return common_pb2.UpdateResp(isPermit = False);
		# 判断数据库是否已有相应工具名，并校验所要上传工具版本号是否为最新
		sql = "SELECT version FROM tool WHERE category = '%s' AND name = '%s' AND common_version = '%s'"%(self.__verifyCategory__(request.category), request.name, request.commonVersion);
		ret, results = _GG("DBCManager").MySQL().execute(sql);
		if not ret:
			for toolInfo in results:
				verList = self._splitVersion_(toolInfo["version"]);
				if verList[1] > toolVerList[1] or (verList[1] == toolVerList[1] and verList[2] >= toolVerList[2]):
					return common_pb2.UploadResp(isPermit = False);
			fileName = self._getFileName_(name = request.name, category = request.category, version = request.version, suffix = "zip");
			tokenStr = json.dumps({
				"host" : _GG("ServerConfig").Config().Get("server", "remote_host"),
				"port" : _GG("ServerConfig").Config().Get("server", "remote_port"),
				"user" : _GG("ServerConfig").Config().Get("upload", "user"),
				"password" : _GG("ServerConfig").Config().Get("upload", "password"),
				"url" : os.path.join(_GG("ServerConfig").Config().Get("upload", "file_dir"), fileName),
			});
			return common_pb2.UploadResp(isPermit = True, token = str.encode(tokenStr));
		return common_pb2.UploadResp(isPermit = False);

	def Uploaded(self, request, context):
		# 校验所传用户ID数据
		sql = "SELECT name FROM user WHERE id = '%d'"%request.uid;
		ret, results = _GG("DBCManager").MySQL().execute(sql);
		if not ret:
			return common_pb2.Resp(isSuccess = False);
		# 判断上传信息是否正确
		toolVerList = self._splitVersion_(request.version);
		if len(toolVerList) != 3:
			return common_pb2.Resp(isSuccess = False);
		# 获取文件地址
		fileName = self._getFileName_(name = request.name, category = request.category, version = request.version, suffix = "zip");
		filePath = os.path.join(_GG("ServerConfig").Config().Get("upload", "file_dir"), fileName);
		# 校验上传的文件是否存在
		if not os.path.exists(filePath):
			return common_pb2.Resp(isSuccess = False);
		# 插入工具信息到数据库中
		url = os.path.join(_GG("ServerConfig").Config().Get("download", "file_addr"), fileName);
		sql = "INSERT INTO tool(uid, key, category, name, version, common_version, description, url, time) VALUES(%d, '%s', '%s', '%s', '%s', '%s', '%s', '%s')"%(
			request.uid, self._getFileName_(name = request.name, category = request.category), self.__verifyCategory__(request.category),
			request.name, request.version, request.commonVersion, request.description,
			url, time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()));
		ret, results = _GG("DBCManager").MySQL().execute(sql);
		if ret:
			return common_pb2.Resp(isSuccess = True);
		return common_pb2.Resp(isSuccess = False);

	def Download(self, request, context):
		# 校验玩家下载请求权限[request.uid]
		# 获取下载数据
		sql = "SELECT tool.name, category, description, version, user.name FROM tool LEFT OUTER JOIN user ON tool.uid = user.id WHERE key = '%s' AND common_version = '%s'"%(request.key, request.commonVersion);
		ret, results = _GG("DBCManager").MySQL().execute(sql);
		if ret:
			result = results[0];
			fileName = self._getFileName_(key = request.key, version = result["version"], suffix = "zip");
			filePath = os.path.join(_GG("ServerConfig").Config().Get("upload", "file_dir"), fileName);
			if os.path.exists(filePath):
				url = os.path.join(_GG("ServerConfig").Config().Get("download", "file_addr"), fileName);
				namePath = "/".join(result["category"], )
				return common_pb2.DownloadResp(isExist = True, url = url, totalSize = os.path.getsize(filePath),
				 toolInfo = common_pb2.DownloadResp.ToolInfo(name = result["name"], category = result["category"],
				 	description = result["description"], version = result["version"], author = result["author"]));
		return common_pb2.DownloadResp(isExist = False);

	def Update(self, request, context):
		# 判断请求信息是否正确
		toolVerList = self._splitVersion_(request.version);
		if len(toolVerList) != 3:
			return common_pb2.UpdateResp(isUpToDate = True);
		# 找到对应common版本的下载链接
		sql = "SELECT version FROM tool WHERE key = '%s' AND common_version = '%s'"%(request.key, request.commonVersion);
		ret, results = _GG("DBCManager").MySQL().execute(sql);
		if ret:
			for toolInfo in results:
				verList = self._splitVersion_(toolInfo["version"]);
				if verList[1] > toolVerList[1] or (verList[1] == toolVerList[1] and verList[2] >= toolVerList[2]):
					fileName = self._getFileName_(key = request.key, version = toolInfo["version"], suffix = "zip");
					filePath = os.path.join(_GG("ServerConfig").Config().Get("upload", "file_dir"), fileName);
					if os.path.exists(filePath):
						url = os.path.join(_GG("ServerConfig").Config().Get("download", "file_addr"), fileName);
						return common_pb2.UpdateResp(isUpToDate = False, 
							updateInfo = common_pb2.DownloadResp(isExist = True, url = url, totalSize = os.path.getsize(filePath)));
		return common_pb2.UpdateResp(isUpToDate = True);

	def Comment(self, request, context):
		# 校验所传用户ID数据
		sql = "SELECT name FROM user WHERE id = '%d'"%request.uid;
		ret, results = _GG("DBCManager").MySQL().execute(sql);
		if not ret:
			return common_pb2.Resp(isSuccess = False);
		# 校验所传用户ID数据
		sql = "SELECT id FROM tool WHERE key = '%s' AND common_version = '%s'"%(request.key, request.commonVersion);
		ret, results = _GG("DBCManager").MySQL().execute(sql);
		if ret:
			# 插入评论信息到数据库中
			sql = "INSERT INTO comment(uid, tkey, version, score, content, time) VALUES(%d, %d, %.1f, '%s', '%s')"%(
				request.uid, request.key, request.version, request.score, request.content,
				time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()));
			ret, results = _GG("DBCManager").MySQL().execute(sql);
			if ret:
				return common_pb2.Resp(isSuccess = True);
		return common_pb2.Resp(isSuccess = False);

	def Collect(self, request, context):
		# 校验所传用户ID数据
		sql = "SELECT name FROM user WHERE id = '%d'"%request.uid;
		ret, results = _GG("DBCManager").MySQL().execute(sql);
		if not ret:
			return common_pb2.Resp(isSuccess = False);
		# 校验所传用户ID数据
		sql = "SELECT id FROM tool WHERE key = '%s' AND common_version = '%s'"%(request.key, request.commonVersion);
		ret, results = _GG("DBCManager").MySQL().execute(sql);
		if ret:
			# 插入收藏信息到数据库中
			sql = "INSERT INTO collection(uid, tkey) VALUES(%d, %d)"%(request.uid, request.key);
			ret, results = _GG("DBCManager").MySQL().execute(sql);
			if ret:
				return common_pb2.Resp(isSuccess = True);
		return common_pb2.Resp(isSuccess = False);
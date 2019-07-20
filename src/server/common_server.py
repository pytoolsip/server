# -*- coding: utf-8 -*-
# @Author: JimDreamHeart
# @Date:   2019-02-23 21:07:59
# @Last Modified by:   JimDreamHeart
# @Last Modified time: 2019-04-20 00:31:29
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

	def _getFilePath_(self, key = "", name = "", category = "", version = "", suffix = ""):
		if not key:
			if category:
				name = self.__verifyCategory__(category) + name;
			key = hashlib.md5(name.encode("utf-8")).hexdigest();
		if version:
			version = "/" + version;
		if suffix and suffix[0] != ".":
			suffix = "." + suffix;
		return "".join([key, version, suffix]);

	def __verifyCategory__(self, category):
		category = category.replace(" ", "");
		if len(category) > 0 and category[-1] != "/":
			category += "/";
		return category;

	def _checkNewestVersion_(verList, toolVerList, isCheckV1 = True, isIncludeEqu = False):
		if isCheckV1 and verList[0] != toolVerList[0]:
			return verList[0] > toolVerList[0];
		if verList[1] != toolVerList[1]:
			return verList[1] > toolVerList[1];
		if verList[2] != toolVerList[2]:
			return verList[2] > toolVerList[2];
		return isIncludeEqu;
	
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
		if _GG("DBCManager").Redis().exists("veri_code_"+request.email) and _GG("DBCManager").Redis().get("veri_code_"+request.email) == request.veriCode:
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

	def Download(self, request, context):
		# 校验玩家下载请求权限[request.uid]
		# 获取下载数据
		sql = "SELECT tool.name, tool.category, tool.description, version, changelog, user.name FROM tool_detail LEFT OUTER JOIN tool ON tool_detail.tkey = tool.tkey LEFT OUTER JOIN user ON tool.uid = user.id WHERE tkey = '%s' AND ip_version = '%s'"%(request.key, request.IPVersion);
		ret, results = _GG("DBCManager").MySQL().execute(sql);
		if ret:
			# 获取最优结果
			bestResult = results[0];
			for i in range(1, len(results)):
				result = results[i];
				if self._checkNewestVersion_(self._splitVersion_(result["version"]), self._splitVersion_(bestResult["version"])):
					bestResult = result;
			_GG("Log").d("Download -> best result:", bestResult);
			# 返回最优结果
			filePath = self._getFilePath_(key = request.key, version = bestResult["version"], suffix = "zip");
			if os.path.exists(os.path.join(_GG("ServerConfig").Config().Get("upload", "file_dir"), filePath)):
				url = os.path.join(_GG("ServerConfig").Config().Get("download", "file_addr"), filePath);
				return common_pb2.DownloadResp(isExist = True, url = url, totalSize = os.path.getsize(filePath),
				 toolInfo = common_pb2.DownloadResp.ToolInfo(name = bestResult["tool.name"], category = bestResult["tool.category"],
				 	description = bestResult["tool.description"], version = bestResult["version"], author = bestResult["user.name"], changelog = bestResult["changelog"]));
		return common_pb2.DownloadResp(isExist = False);

	def Update(self, request, context):
		# 判断请求信息是否正确
		toolVerList = self._splitVersion_(request.version);
		if len(toolVerList) != 3:
			_GG("Log").d("Update -> verify version failed！", request.version);
			return common_pb2.UpdateResp(isUpToDate = True);
		# 找到对应平台版本的下载链接
		sql = "SELECT version FROM tool_detail WHERE tkey = '%s' AND ip_version = '%s'"%(request.key, request.IPVersion);
		ret, results = _GG("DBCManager").MySQL().execute(sql);
		for toolInfo in results:
			if self._checkNewestVersion_(self._splitVersion_(toolInfo["version"]), toolVerList):
				filePath = self._getFilePath_(key = request.key, version = toolInfo["version"], suffix = "zip");
				if os.path.exists(os.path.join(_GG("ServerConfig").Config().Get("upload", "file_dir"), filePath)):
					url = os.path.join(_GG("ServerConfig").Config().Get("download", "file_addr"), filePath);
					return common_pb2.UpdateResp(isUpToDate = False, 
						updateInfo = common_pb2.DownloadResp(isExist = True, url = url, totalSize = os.path.getsize(filePath)));
		return common_pb2.UpdateResp(isUpToDate = True);

	def UpdateIP(self, request, context):
		# 判断请求信息是否正确
		ptipVerList = self._splitVersion_(request.version);
		if len(ptipVerList) != 3:
			_GG("Log").d("UpdateIP -> verify version failed！", request.version);
			return common_pb2.UpdateIPResp(isUpToDate = True);
		# 判断是否需要更新
		ret, results = _GG("DBCManager").MySQL().execute("SELECT update_version, update_url, update_size, update_type FROM ptip WHERE version = '%s'"%request.version);
		if ret and results[0]["update_version"] != request.version:
			# 返回平台更新信息
			ptipInfo = results[0];
			return common_pb2.UpdateIPResp(isUpToDate = False, url = ptipInfo["update_url"], totalSize = ptipInfo["update_size"], isAllowQuit = ptipInfo["update_type"]>1);
		return common_pb2.UpdateIPResp(isUpToDate = True);
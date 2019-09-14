# -*- coding: utf-8 -*-
# @Author: JimDreamHeart
# @Date:   2019-02-23 21:07:59
# @Last Modified by:   JimDreamHeart
# @Last Modified time: 2019-04-20 00:31:29
import os,json,time;
import hashlib;
from urllib import request;

from _Global import _GG;
from net import common_pb2,common_pb2_grpc;

from constant import RespCode;
from function import random_util;

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
		retDate = {"code" : RespCode.FAILED.value, "data" : b""};
		methodName = request.key;
		if methodName in self.__methodDict:
			isSuccess, data = self.__methodDict[methodName](json.loads(bytes.decode(request.data)), context);
			if isSuccess:
				 retDate["code"] = RespCode.SUCCESS.value;
			retDate["data"] = str.encode(json.dumps(data));
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

	# 获取最优结果
	def _getBeseResult_(self, results):
		bestResult = results[0];
		for i in range(1, len(results)):
			result = results[i];
			if self._checkNewestVersion_(self._splitVersion_(result["version"]), self._splitVersion_(bestResult["version"])):
				bestResult = result;
		return bestResult;
		
	# 获取url文件大小
	def _getUrlFileSize_(self, url):
		try:
			resp = request.urlopen(url);
			return int(resp.headers['content-length']);
		except Exception as e:
			_GG("Log").w(f"Failed to get size by url[{url}]!", e);
		return -1;
	
	def Login(self, request, context):
		name, pwd = request.name, _GG("DecodeStr")(request.pwd);
		if not request.isAuto:
			ret, results = _GG("DBCManager").MySQL().execute("SELECT salt FROM user WHERE name = '%s'"%name);
			if ret:
				pwd = hashlib.md5("|".join([results[0]["salt"], pwd]).encode("utf-8")).hexdigest();
			elif _GG("DBCManager").Redis().exists(pwd):
				pwd = _GG("DBCManager").Redis().get(pwd); # 从缓存中读取密码
		# 从数据库中获取用户信息
		sql = "SELECT * FROM user WHERE name = '%s' AND password = '%s'"%(name, pwd);
		ret, results = _GG("DBCManager").MySQL().execute(sql);
		if ret:
			userInfo = results[0];
			# 生成索要缓存的密码Md5
			randMulti = random_util.randomMulti(12); # 12位随机数
			pwdMd5 = hashlib.md5("|".join([userInfo["password"], randMulti]).encode("utf-8")).hexdigest();
			# 缓存密码信息
			expire = 10*24*60*60; # 缓存10天
			_GG("DBCManager").Redis().set(pwdMd5, userInfo["password"], expire);
			return common_pb2.LoginResp(code = RespCode.SUCCESS.value, expire = expire, 
				userInfo = common_pb2.UserInfo(uid = userInfo["id"], pwd = pwdMd5, email = userInfo["email"]));
		return common_pb2.LoginResp(code = RespCode.LOGIN_FAILED.value);

	def Download(self, request, context):
		# 获取下载数据
		sql = "SELECT tool.name, tool.category, tool.description, version, changelog, file_path, user.name FROM tool_detail LEFT OUTER JOIN tool ON tool_detail.tkey = tool.tkey LEFT OUTER JOIN user ON tool.uid = user.id WHERE tool.tkey = '%s' AND ip_base_version = '%s'"%(request.key, request.IPBaseVer);
		ret, results = _GG("DBCManager").MySQL().execute(sql);
		if ret:
			# 获取最优结果
			bestResult = self._getBeseResult_(results);
			_GG("Log").d("Download -> best result:", bestResult);
			# 返回最优结果
			filePath = bestResult["file_path"];
			url = "/".join([_GG("ServerConfig").Config().Get("download", "tools_dir_url"), filePath]);
			fileSize = self._getUrlFileSize_(url);
			_GG("Log").d("Download -> get url info:", url, fileSize);
			if fileSize > 0:
				# 缓存下载键值
				randMulti = random_util.randomMulti(12); # 12位随机数
				downloadKey = hashlib.md5("|".join([request.key, randMulti]).encode("utf-8")).hexdigest();
				_GG("DBCManager").Redis().set(downloadKey, request.key, 12*60*60); # 缓存12小时
				# 返回下载数据
				return common_pb2.DownloadResp(code = RespCode.SUCCESS.value, url = url, totalSize = fileSize, downloadKey = downloadKey, 
				 toolInfo = common_pb2.ToolInfo(tkey = request.key, name = bestResult["tool.name"], category = bestResult["tool.category"],
				 	description = bestResult["tool.description"], version = bestResult["version"], changelog = bestResult["changelog"], author = bestResult["user.name"]));
		return common_pb2.DownloadResp(code = RespCode.DOWNLOAD_FAILED.value);

	def Update(self, request, context):
		# 判断请求信息是否正确
		toolVerList = self._splitVersion_(request.version);
		if len(toolVerList) != 3:
			_GG("Log").d("Update -> verify version failed！", request.version);
			return common_pb2.UpdateResp(code = RespCode.UPDATE_FAILED.value);
		# 找到对应平台版本的下载链接
		sql = "SELECT version, file_path FROM tool_detail WHERE tkey = '%s' AND ip_base_version = '%s'"%(request.key, request.IPBaseVer);
		ret, results = _GG("DBCManager").MySQL().execute(sql);
		if ret:
			# 获取最优结果
			bestResult = self._getBeseResult_(results);
			_GG("Log").d("Update -> best result:", bestResult);
			if bestResult["version"] != request.version:
				# 返回最优结果
				filePath = bestResult["file_path"];
				url = "/".join([_GG("ServerConfig").Config().Get("download", "tools_dir_url"), filePath]);
				fileSize = self._getUrlFileSize_(url);
				_GG("Log").d("Update -> get url info:", url, fileSize);
				if fileSize > 0:
					return common_pb2.DownloadResp(code = RespCode.SUCCESS.value, url = url, totalSize = fileSize);
		return common_pb2.UpdateResp(code = RespCode.UPDATE_FAILED.value);

	def UpdateIP(self, request, context):
		# 判断请求信息是否正确
		ptipVerList = self._splitVersion_(request.version);
		if len(ptipVerList) != 3:
			_GG("Log").d("UpdateIP -> verify version failed！", request.version);
			return common_pb2.UpdateIPResp(code = RespCode.UPDATE_FAILED.value);
		# 获取最优版本的平台信息
		def getBestVerPtip(base_version):
			ret, results = _GG("DBCManager").MySQL().execute("SELECT update_version, version, file_path, exe_list FROM ptip WHERE base_version = '%s'"%base_version);
			if ret:
				# 获取最优结果
				bestResult = self._getBeseResult_(results);
				# 判断是否有更新版本
				if bestResult["update_version"] != base_version:
					return getBestVerPtip(bestResult["update_version"]);
				return bestResult;
			return None;
		# 判断是否需要更新
		bestResult = getBestVerPtip(".".join([str(ver) for ver in ptipVerList[:2]]));
		if bestResult:
			_GG("Log").d("UpdateIP -> best result:", bestResult);
			bestVersion = bestResult["version"];
			if bestVersion != request.version:
				# 返回请求结果
				return common_pb2.UpdateIPResp(code = RespCode.SUCCESS.value, version = bestVersion);
		return common_pb2.UpdateIPResp(code = RespCode.UPDATE_FAILED.value);

	def ReqToolInfo(self, request, context):
		if request.key:
			sql = "SELECT tool.name, category, description, version, changelog, user.name FROM tool_detail INNER JOIN tool ON tool_detail.tkey = tool.tkey INNER JOIN user ON tool.uid = user.id WHERE tool.tkey = '%s' AND ip_base_version = '%s' ORDER BY tool_detail.time"%(request.key, request.IPBaseVer);
			ret, results = _GG("DBCManager").MySQL().execute(sql);
			if ret:
				bestResult = results[0];
				return common_pb2.ToolInfoResp(code = RespCode.SUCCESS.value, toolInfo = common_pb2.ToolInfo(tkey = request.key, name = bestResult["name"],
				category = bestResult["category"], description = bestResult["description"], version = bestResult["version"], changelog = bestResult["changelog"], author = bestResult["user.name"]));
		# 返回对应平台基础版本的所有工具信息
		sql = "SELECT tool.name, category, description, tool.tkey, version, changelog, user.name FROM tool_detail INNER JOIN tool ON tool_detail.tkey = tool.tkey INNER JOIN user ON tool.uid = user.id WHERE ip_base_version = '%s' ORDER BY tool_detail.time"%request.IPBaseVer;
		ret, results = _GG("DBCManager").MySQL().execute(sql);
		if ret:
			toolInfos = [];
			for result in results:
				toolInfos.append(common_pb2.ToolInfo(tkey = result["tkey"], name = result["name"], category = result["category"], description = result["description"], 
				version = result["version"], changelog = result["changelog"], author = result["user.name"]));
			return common_pb2.ToolInfoResp(code = RespCode.SUCCESS.value, toolList = toolInfos);
		return common_pb2.ToolInfoResp(code = RespCode.UPDATE_FAILED.value);

	def DownloadRecord(self, request, context):
		# 更新工具的下载数据
		if _GG("DBCManager").Redis().exists(request.downloadKey):
			tkey = _GG("DBCManager").Redis().get(request.downloadKey); # 从缓存中读取下载key值
			if tkey == request.key:
				ret, results = _GG("DBCManager").MySQL().execute("UPDATE tool SET download = download + 1 WHERE tkey = '%s'"%request.key);
				if ret:
					return common_pb2.Resp(code = RespCode.SUCCESS.value);
			_GG("DBCManager").Redis().delete(request.downloadKey); # 从缓存中删除下载key值
		return common_pb2.Resp(code = RespCode.FAILED.value);

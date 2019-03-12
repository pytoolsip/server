# -*- coding: utf-8 -*-
# @Author: JimDreamHeart
# @Date:   2019-02-23 21:07:59
# @Last Modified by:   JimDreamHeart
# @Last Modified time: 2019-03-09 20:46:27
import os,json;

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

	def splitVersion(self, version):
		vers = version.split(".");
		verList = [];
		for ver in vers:
			verList.append(int(ver));
		return verList;

	def Request(self, request, context):
		retDate = {"isSuccess" : False};
		methodName = request.key;
		if methodName in self.__methodDict:
			isSuccess, data = self.__methodDict[methodName](json.loads(bytes.decode(request.data)), context);
			retDate = {
				"isSuccess" : bool(isSuccess),
				"data" : str.encode(json.dumps(data)),
			};
		return common_pb2.Res(**retDate);
	
	def Login(self, request, context):
		sql = "SELECT * FROM users WHERE name = '%s' AND password = '%s'"%(request.name, request.password);
		ret, results = _GG("DBCManager").execute(sql);
		if ret:
			userInfo = results[0];
			return common_pb2.LoginRes(isSuccess = True, name = userInfo["name"], email = userInfo["email"]);
		return common_pb2.LoginRes(isSuccess = False);

	def Register(self, request, context):
		# 校验提交的信息中是否已存在于数据库中
		sql = "SELECT id FROM users WHERE name = '%s'"%request.name;
		ret, results = _GG("DBCManager").execute(sql);
		if ret:
			return common_pb2.Res(isSuccess = False);
		# 插入注册数据到数据库中
		sql = "INSERT INTO users(name, password, email) VALUES(%s, %s, %s)"%(request.name, request.password, request.email);
		ret, results = _GG("DBCManager").execute(sql);
		return common_pb2.Res(isSuccess = ret);

	def Upload(self, request, context):
		# 判断上传信息是否正确
		toolVerList = self.splitVersion(request.version);
		if len(toolVerList) != 4:
			return common_pb2.UploadRes(isPermit = False);
		# 判断数据库是否已有相应工具名，并校验所要上传工具版本号是否为最新
		sql = "SELECT version FROM tools WHERE name = '%s' And common_version = '%s'"%(request.name, ".".join(toolVerList[:2]));
		_, results = _GG("DBCManager").execute(sql);
		if len(results) > 0:
			for toolInfo in results:
				verList = self.splitVersion(toolInfo["version"]);
				if verList[2] > toolVerList[2] or (verList[2] == toolVerList[2] and verList[3] >= toolVerList[3]):
					return common_pb2.UploadRes(isPermit = False);
		tokenStr = json.dumps({
			"host" : _GG("ServerConfig").Config().Get("server", "host"),
			"port" : _GG("ServerConfig").Config().Get("server", "port"),
			"user" : _GG("ServerConfig").Config().Get("upload", "user"),
			"password" : _GG("ServerConfig").Config().Get("upload", "password"),
			"fileName" : "%s_%s.zip"%(request.name, request.version),
		});
		return common_pb2.UploadRes(isPermit = True, token = str.encode(tokenStr));

	def Uploaded(self, request, context):
		# 校验所传用户ID数据
		sql = "SELECT name FROM users WHERE id = '%s'"%request.uid;
		ret, results = _GG("DBCManager").execute(sql);
		if ret:
			return common_pb2.Res(isSuccess = False);
		# 判断上传信息是否正确
		toolVerList = self.splitVersion(request.version);
		if len(toolVerList) != 4:
			return common_pb2.Res(isSuccess = False);
		# 校验上传的文件是否存在
		filePath = _GG("ServerConfig").Config().Get("download", "upload_dir") + "%s_%s.zip"%(request.name, request.version);
		if not os.path.exists(filePath):
			return common_pb2.Res(isSuccess = False);
		# 插入工具信息到数据库中
		sql = "INSERT INTO tools(uid, name, version, common_version) VALUES(%d, %s, %s, %s)"%(request.uid, request.name, request.version, ".".join(toolVerList[:2]));
		ret, results = _GG("DBCManager").execute(sql);
		if ret:
			return common_pb2.Res(isSuccess = True);

	def Download(self, request, context):
		sql = "SELECT id FROM tools WHERE name = '%s' AND version = '%s'"%(request.name, request.version);
		ret, results = _GG("DBCManager").execute(sql);
		if ret:
			fileName = "%s_%s.zip"%(request.name, request.version);
			totalSize = os.path.getsize(_GG("ServerConfig").Config().Get("download", "upload_dir") + fileName);
			url = _GG("ServerConfig").Config().Get("download", "files_addr");
			return common_pb2.DownloadRes(isExist = True, url = url + fileName, totalSize = totalSize);
		return common_pb2.DownloadRes(isExist = False);

	def Update(self, request, context):
		# 判断请求信息是否正确
		toolVerList = self.splitVersion(request.version);
		if len(toolVerList) != 4:
			return common_pb2.UpdateRes(isUpToDate = True);
		# 找到对应common版本的下载链接
		sql = "SELECT version FROM tools WHERE name = '%s' And common_version = '%s'"%(request.name, ".".join(toolVerList[:2]));
		ret, results = _GG("DBCManager").execute(sql);
		if ret:
			for toolInfo in results:
				verList = self.splitVersion(toolInfo["version"]);
				if verList[2] < toolVerList[2] or (verList[2] == toolVerList[2] and verList[3] < toolVerList[3]):
					fileName = "%s_%s.zip"%(request.name, request.version);
					totalSize = os.path.getsize(_GG("ServerConfig").Config().Get("download", "upload_dir") + fileName);
					url = _GG("ServerConfig").Config().Get("download", "files_addr");
					return common_pb2.UpdateRes(isUpToDate = False, 
						updateInfo = common_pb2.DownloadRes(isExist = True, url = url + fileName, totalSize = totalSize));
		return common_pb2.UpdateRes(isUpToDate = True);
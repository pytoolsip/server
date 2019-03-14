# -*- coding: utf-8 -*-
# @Author: JimZhang
# @Date:   2019-03-01 21:16:40
# @Last Modified by:   JimDreamHeart
# @Last Modified time: 2019-03-14 20:26:52

from _Global import _GG;
from net.proto import common_pb2,common_pb2_grpc;

def ExtendSrvMethod():
	_GG("MainServer").registerMethod("RequestToolInfos", RequestToolInfos);
	_GG("MainServer").registerMethod("VertifyToolName", VertifyToolName);
	_GG("MainServer").registerMethod("VertifyUserName", VertifyUserName);
	_GG("MainServer").registerMethod("VertifyUserEmail", VertifyUserEmail);
	pass;

def RequestToolInfos(data, context):
	sql = "SELECT tool.name, version, detail, user.name FROM tool LEFT OUTER JOIN user ON tool.uid = user.id WHERE common_version = '%s'"%data.get("commonVersion", "");
	ret, retData = _GG("DBCManager").execute(sql);
	if not ret:
		return False, [];
	return True, [{
		"title" : info["name"],
		"version" : info["version"],
		"detail" : info["detail"] and info["detail"] or "",
		"userName" : info["user.name"],
	} for info in retData];

def VertifyToolName(data, context):
	sql = "SELECT id FROM tool WHERE name = '%s' AND common_version = '%s'"%(data.get("name", ""), data.get("commonVersion", ""));
	return _GG("DBCManager").execute(sql);

def VertifyUserName(data, context):
	sql = "SELECT id FROM user WHERE name = '%s'"%data.get("name", "");
	return _GG("DBCManager").execute(sql);

def VertifyUserEmail(data, context):
	sql = "SELECT id FROM user WHERE email = '%s'"%data.get("email", "");
	return _GG("DBCManager").execute(sql);
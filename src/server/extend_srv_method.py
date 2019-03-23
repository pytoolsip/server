# -*- coding: utf-8 -*-
# @Author: JimZhang
# @Date:   2019-03-01 21:16:40
# @Last Modified by:   JimDreamHeart
# @Last Modified time: 2019-03-23 15:27:21
import random;
import smtplib;
from email.mime.text import MIMEText;

from _Global import _GG;
from net.proto import common_pb2,common_pb2_grpc;

def ExtendSrvMethod():
	_GG("MainServer").registerMethod("RequestToolInfos", RequestToolInfos);
	_GG("MainServer").registerMethod("VertifyToolName", VertifyToolName);
	_GG("MainServer").registerMethod("VertifyUserName", VertifyUserName);
	_GG("MainServer").registerMethod("VertifyUserEmail", VertifyUserEmail);
	_GG("MainServer").registerMethod("VertifyVerificationCode", VertifyVerificationCode);
	_GG("MainServer").registerMethod("SendVerificationCode", SendVerificationCode);
	pass;

def RequestToolInfos(data, context):
	sql = "SELECT tool.name, version, description, user.name FROM tool LEFT OUTER JOIN user ON tool.uid = user.id WHERE common_version = '%s'"%data.get("commonVersion", "");
	ret, retData = _GG("DBCManager").MySQL().execute(sql);
	if ret:
		return True, [{
			"title" : info["name"],
			"version" : info["version"],
			"detail" : info["description"],
			"userName" : info["user.name"],
		} for info in retData];
	return False, [];

def VertifyToolName(data, context):
	sql = "SELECT uid,version FROM tool WHERE category = '%s' AND name = '%s' AND common_version = '%s'"%(data.get("category", ""), data.get("name", ""), data.get("commonVersion", ""));
	ret,retData = _GG("DBCManager").MySQL().execute(sql);
	if ret:
		if retData[0]["uid"] == data.get("uid", -1):
			return True, {"version" : retData[0]["version"]};
		return False, {}; # 校验失败，存在相同工具名，却不同玩家的工具数据
	return True, {};

def VertifyUserName(data, context):
	sql = "SELECT id FROM user WHERE name = '%s'"%data.get("name", "");
	return _GG("DBCManager").MySQL().execute(sql);

def VertifyUserEmail(data, context):
	sql = "SELECT id FROM user WHERE email = '%s'"%data.get("email", "");
	return _GG("DBCManager").MySQL().execute(sql);

def VertifyVerificationCode(data, context):
	# 校验是否存在验证码相关信息
	if "email" not in data or "code" not in data:
		return False, {};
	# 校验验证码
	if _GG("DBCManager").Redis().hexists("verification_code", data["email"]) and _GG("DBCManager").Redis().hget("verification_code", data["email"]) == data["code"]:
		return True, {};
	return False, {};

def SendVerificationCode(data, context):
	# 校验是否存在邮箱信息
	if "email" not in data:
		return False, {};
	# 生成六位数验证码
	code = "".join(random.sample(range(10), 6));
	# 保存验证码
	expire = 60; # 有效期：60s
	_GG("DBCManager").Redis().hset("verification_code", data["email"], code, ex = expire);
	# 发送验证码到指定邮箱
	return sendEmailContent(data["email"], "PyToolsIp 验证", "验证码："+code), {"expire" : expire};

def sendEmailContent(email, title, content):
	srvConf = _GG("ServerConfig").Config(); # 服务配置
	# 构建发送消息
	message = MIMEText(content,"plain","utf-8");
	message["Subject"] = title;
	message['From'] = srvConf.Get("email", "user_mail");
	message['To'] = email;
	#登录并发送邮件
	smtpObj = smtplib.SMTP();
	smtpObj.connect(srvConf.Get("email", "host"), int(srvConf.Get("email", "port")));
	smtpObj.login(srvConf.Get("email", "user_mail"), srvConf.Get("email", "password"));
	try:
		smtpObj.sendmail(srvConf.Get("email", "user_mail"), [email], message.as_string());
		return True;
	except Exception as e:
		_GG("Log").e("Send mail failed ! =>", e);
		return False;
	finally:
		smtpObj.quit();

# -*- coding: utf-8 -*-
# @Author: JimZhang
# @Date:   2019-03-01 21:16:40
# @Last Modified by:   JimDreamHeart
# @Last Modified time: 2019-04-20 00:17:13
import hashlib;
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
	_GG("MainServer").registerMethod("RequestToolInfo", RequestToolInfo);
	pass;

def RequestToolInfos(data, context):
	sql = "SELECT tool.name, category, description, tool.tkey, version, changelog, user.name FROM tool_detail INNER JOIN tool ON tool_detail.tkey = tool.tkey INNER JOIN user ON tool.uid = user.id WHERE common_version = '%s' ORDER BY tool_detail.time"%data.get("commonVersion", "");
	ret, retData = _GG("DBCManager").MySQL().execute(sql);
	if ret:
		return True, [{
			"key" : info["tkey"],
			"title" : info["name"],
			"category" : info["category"],
			"description" : info["description"],
			"version" : info["version"],
			"changelog" : info["changelog"],
			"author" : info["user.name"],
		} for info in retData];
	return False, [];

def VertifyToolName(data, context):
	if not data.get("fullName", None):
		return False, {"tips" : "校验字段不正确！"}; # 校验失败，不存在校验数据
	tkey = hashlib.md5(data["fullName"].encode("utf-8")).hexdigest();
	sql = "SELECT uid,version FROM tool_detail INNER JOIN tool ON tool_detail.tkey = tool.tkey WHERE tkey = '%s'"%tkey;
	ret,retData = _GG("DBCManager").MySQL().execute(sql);
	if ret:
		if retData[0]["uid"] == data.get("uid", -1):
			return True, {"version" : retData[0]["version"]};
		return False, {"tips" : "已存在相同工具名，且您不是此工具的提交者！"}; # 校验失败，存在相同工具名，却不同玩家的工具数据
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
	if _GG("DBCManager").Redis().exists("veri_code_"+data["email"]) and _GG("DBCManager").Redis().get("veri_code_"+data["email"]) == data["code"]:
		return True, {};
	return False, {};

def SendVerificationCode(data, context):
	# 校验是否存在邮箱信息
	if "email" not in data:
		return False, {};
	# 生成六位数验证码
	code = "".join([str(i) for i in random.sample(range(10), 6)]);
	# 保存验证码
	expire = int(_GG("ServerConfig").Config().Get("email", "expire", 60)); # 默认有效期：60s
	_GG("DBCManager").Redis().set("veri_code_"+data["email"], code, ex = expire);
	# 发送验证码到指定邮箱
	return sendEmailContent(data["email"], "PyToolsIp 验证", "验证码："+code), {"expire" : expire};

def sendEmailContent(email, title, content):
	srvConf = _GG("ServerConfig").Config(); # 服务配置
	# 构建发送消息
	message = MIMEText(content,"plain","utf-8");
	message["Subject"] = title;
	message['From'] = srvConf.Get("email", "user_mail");
	message['To'] = email;
	try:
		#登录并发送邮件
		smtpObj = smtplib.SMTP_SSL(srvConf.Get("email", "host"), int(srvConf.Get("email", "port")));
		smtpObj.login(srvConf.Get("email", "user_mail"), srvConf.Get("email", "password"));
		smtpObj.sendmail(srvConf.Get("email", "user_mail"), [email], message.as_string());
		smtpObj.quit();
		return True;
	except smtplib.SMTPException as e:
		_GG("Log").e("Send mail failed ! =>", e);
	return False;

def RequestToolInfo(data, context):
	sql = "SELECT tool.name, category, description, version, changelog, user.name FROM tool_detail INNER JOIN tool ON tool_detail.tkey = tool.tkey INNER JOIN user ON tool.uid = user.id WHERE tkey = '%s' AND common_version = '%s' ORDER BY tool_detail.time"%(data.get("key", ""), data.get("commonVersion", ""));
	ret, retData = _GG("DBCManager").MySQL().execute(sql);
	if ret:
		info = retData[0];
		return True, {
			"title" : info["name"],
			"category" : info["category"],
			"description" : info["description"],
			"version" : info["version"],
			"changelog" : info["changelog"],
			"author" : info["user.name"],
		};
	return False, {};

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
from net import common_pb2,common_pb2_grpc;

def ExtendSrvMethod():
	_GG("MainServer").registerMethod("ReqPublicKey", ReqPublicKey);
	pass;

# 请求公钥数据
def ReqPublicKey(data, context):
	return True, {"key" : _GG("g_PublicKey")};
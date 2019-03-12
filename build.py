# -*- coding: utf-8 -*-
# @Author: JimDreamHeart
# @Date:   2019-03-12 23:49:20
# @Last Modified by:   JimDreamHeart
# @Last Modified time: 2019-03-13 00:29:33
import os,json;

# 校验依赖模块
def verifyDepends():
	dependJson = os.path.abspath(os.path.join(os.path.dirname(__file__),"depend.json"));
	if os.path.exists(dependJson):
		with open(dependJson, "r") as f:
			dependList = json.loads(f.read());
			for depend in dependList:
				if os.system("pip show " + depend) != 0:
					os.system("pip install " + depend);

if __name__ == '__main__':
	verifyDepends();
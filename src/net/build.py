# -*- coding: utf-8 -*-
# @Author: JimZhang
# @Date:   2019-02-23 18:52:45
# @Last Modified by:   JimDreamHeart
# @Last Modified time: 2019-02-23 23:01:30
import os;

if __name__ == '__main__':
	os.system("python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. ./proto/common.proto");
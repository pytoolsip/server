# -*- coding: utf-8 -*-
# @Author: JimZhang
# @Date:   2019-02-24 05:10:12
# @Last Modified by:   JimZhang
# @Last Modified time: 2019-03-02 18:33:45

import os;
import sys;

CURRENT_PATH = os.path.dirname(os.path.realpath(__file__));
sys.path.append(CURRENT_PATH);

__all__ = ["CommonServer", "ExtendSrvMethod"];

try:
	from common_server import CommonServer;
	from ext_srv_method import ExtendSrvMethod;

except Exception as e:
	raise e;
finally:
	sys.path.remove(CURRENT_PATH);
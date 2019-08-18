import os;
import sys;

CURRENT_PATH = os.path.dirname(os.path.realpath(__file__));
sys.path.append(CURRENT_PATH);

__all__ = ["common_pb2", "common_pb2_grpc"];

try:
	from proto import common_pb2, common_pb2_grpc;

except Exception as e:
	raise e;
finally:
	sys.path.remove(CURRENT_PATH);
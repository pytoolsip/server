from enum import Enum, unique;

# 枚举应答吗
@unique
class RespCode(Enum):
    SUCCESS = 0; # 请求成功
    FAILED = 0x10; # 请求失败
    LOGIN_FAILED = 0x11; # 登陆失败
    DOWNLOAD_FAILED = 0x12; # 下载失败
    UPDATE_FAILED = 0x13; # 更新失败
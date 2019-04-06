# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: proto/common.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='proto/common.proto',
  package='pbcommon',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x12proto/common.proto\x12\x08pbcommon\" \n\x03Req\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x0c\n\x04\x64\x61ta\x18\x02 \x01(\x0c\"\'\n\x04Resp\x12\x11\n\tisSuccess\x18\x01 \x01(\x08\x12\x0c\n\x04\x64\x61ta\x18\x02 \x01(\x0c\"*\n\x08LoginReq\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x10\n\x08password\x18\x02 \x01(\t\"4\n\x08UserInfo\x12\x0b\n\x03uid\x18\x01 \x01(\x05\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\r\n\x05\x65mail\x18\x03 \x01(\t\"D\n\tLoginResp\x12\x11\n\tisSuccess\x18\x01 \x01(\x08\x12$\n\x08userInfo\x18\x02 \x01(\x0b\x32\x12.pbcommon.UserInfo\"N\n\x0bRegisterReq\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x10\n\x08password\x18\x02 \x01(\t\x12\r\n\x05\x65mail\x18\x03 \x01(\t\x12\x10\n\x08veriCode\x18\x04 \x01(\t\"u\n\tUploadReq\x12\x0b\n\x03uid\x18\x01 \x01(\x05\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x0f\n\x07version\x18\x03 \x01(\t\x12\x15\n\rcommonVersion\x18\x04 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x05 \x01(\t\x12\x10\n\x08\x63\x61tegory\x18\x06 \x01(\t\"-\n\nUploadResp\x12\x10\n\x08isPermit\x18\x01 \x01(\x08\x12\r\n\x05token\x18\x02 \x01(\x0c\">\n\x0b\x44ownloadReq\x12\x0b\n\x03uid\x18\x01 \x01(\x05\x12\x0b\n\x03key\x18\x02 \x01(\t\x12\x15\n\rcommonVersion\x18\x03 \x01(\t\"\xd4\x01\n\x0c\x44ownloadResp\x12\x0f\n\x07isExist\x18\x01 \x01(\x08\x12\x0b\n\x03url\x18\x02 \x01(\t\x12\x11\n\ttotalSize\x18\x03 \x01(\x03\x12\x31\n\x08toolInfo\x18\x04 \x01(\x0b\x32\x1f.pbcommon.DownloadResp.ToolInfo\x1a`\n\x08ToolInfo\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x10\n\x08\x63\x61tegory\x18\x02 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x03 \x01(\t\x12\x0f\n\x07version\x18\x04 \x01(\t\x12\x0e\n\x06\x61uthor\x18\x05 \x01(\t\"M\n\tUpdateReq\x12\x0b\n\x03uid\x18\x01 \x01(\x05\x12\x0b\n\x03key\x18\x02 \x01(\t\x12\x0f\n\x07version\x18\x03 \x01(\t\x12\x15\n\rcommonVersion\x18\x04 \x01(\t\"L\n\nUpdateResp\x12\x12\n\nisUpToDate\x18\x01 \x01(\x08\x12*\n\nupdateInfo\x18\x02 \x01(\x0b\x32\x16.pbcommon.DownloadResp\"n\n\nCommentReq\x12\x0b\n\x03uid\x18\x01 \x01(\x05\x12\x0b\n\x03key\x18\x02 \x01(\t\x12\x0f\n\x07version\x18\x03 \x01(\t\x12\x15\n\rcommonVersion\x18\x04 \x01(\t\x12\r\n\x05score\x18\x05 \x01(\x02\x12\x0f\n\x07\x63ontent\x18\x06 \x01(\t\"N\n\nCollectReq\x12\x0b\n\x03uid\x18\x01 \x01(\x05\x12\x0b\n\x03key\x18\x02 \x01(\t\x12\x0f\n\x07version\x18\x03 \x01(\t\x12\x15\n\rcommonVersion\x18\x04 \x01(\t2\xcf\x03\n\x06\x43ommon\x12(\n\x07Request\x12\r.pbcommon.Req\x1a\x0e.pbcommon.Resp\x12\x30\n\x05Login\x12\x12.pbcommon.LoginReq\x1a\x13.pbcommon.LoginResp\x12\x31\n\x08Register\x12\x15.pbcommon.RegisterReq\x1a\x0e.pbcommon.Resp\x12\x33\n\x06Upload\x12\x13.pbcommon.UploadReq\x1a\x14.pbcommon.UploadResp\x12/\n\x08Uploaded\x12\x13.pbcommon.UploadReq\x1a\x0e.pbcommon.Resp\x12\x39\n\x08\x44ownload\x12\x15.pbcommon.DownloadReq\x1a\x16.pbcommon.DownloadResp\x12\x33\n\x06Update\x12\x13.pbcommon.UpdateReq\x1a\x14.pbcommon.UpdateResp\x12/\n\x07\x43omment\x12\x14.pbcommon.CommentReq\x1a\x0e.pbcommon.Resp\x12/\n\x07\x43ollect\x12\x14.pbcommon.CollectReq\x1a\x0e.pbcommon.Respb\x06proto3')
)




_REQ = _descriptor.Descriptor(
  name='Req',
  full_name='pbcommon.Req',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='pbcommon.Req.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='pbcommon.Req.data', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=32,
  serialized_end=64,
)


_RESP = _descriptor.Descriptor(
  name='Resp',
  full_name='pbcommon.Resp',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='isSuccess', full_name='pbcommon.Resp.isSuccess', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='pbcommon.Resp.data', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=66,
  serialized_end=105,
)


_LOGINREQ = _descriptor.Descriptor(
  name='LoginReq',
  full_name='pbcommon.LoginReq',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='pbcommon.LoginReq.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='password', full_name='pbcommon.LoginReq.password', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=107,
  serialized_end=149,
)


_USERINFO = _descriptor.Descriptor(
  name='UserInfo',
  full_name='pbcommon.UserInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='uid', full_name='pbcommon.UserInfo.uid', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='pbcommon.UserInfo.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='email', full_name='pbcommon.UserInfo.email', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=151,
  serialized_end=203,
)


_LOGINRESP = _descriptor.Descriptor(
  name='LoginResp',
  full_name='pbcommon.LoginResp',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='isSuccess', full_name='pbcommon.LoginResp.isSuccess', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='userInfo', full_name='pbcommon.LoginResp.userInfo', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=205,
  serialized_end=273,
)


_REGISTERREQ = _descriptor.Descriptor(
  name='RegisterReq',
  full_name='pbcommon.RegisterReq',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='pbcommon.RegisterReq.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='password', full_name='pbcommon.RegisterReq.password', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='email', full_name='pbcommon.RegisterReq.email', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='veriCode', full_name='pbcommon.RegisterReq.veriCode', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=275,
  serialized_end=353,
)


_UPLOADREQ = _descriptor.Descriptor(
  name='UploadReq',
  full_name='pbcommon.UploadReq',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='uid', full_name='pbcommon.UploadReq.uid', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='pbcommon.UploadReq.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='version', full_name='pbcommon.UploadReq.version', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='commonVersion', full_name='pbcommon.UploadReq.commonVersion', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='description', full_name='pbcommon.UploadReq.description', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='category', full_name='pbcommon.UploadReq.category', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=355,
  serialized_end=472,
)


_UPLOADRESP = _descriptor.Descriptor(
  name='UploadResp',
  full_name='pbcommon.UploadResp',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='isPermit', full_name='pbcommon.UploadResp.isPermit', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='token', full_name='pbcommon.UploadResp.token', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=474,
  serialized_end=519,
)


_DOWNLOADREQ = _descriptor.Descriptor(
  name='DownloadReq',
  full_name='pbcommon.DownloadReq',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='uid', full_name='pbcommon.DownloadReq.uid', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='key', full_name='pbcommon.DownloadReq.key', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='commonVersion', full_name='pbcommon.DownloadReq.commonVersion', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=521,
  serialized_end=583,
)


_DOWNLOADRESP_TOOLINFO = _descriptor.Descriptor(
  name='ToolInfo',
  full_name='pbcommon.DownloadResp.ToolInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='pbcommon.DownloadResp.ToolInfo.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='category', full_name='pbcommon.DownloadResp.ToolInfo.category', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='description', full_name='pbcommon.DownloadResp.ToolInfo.description', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='version', full_name='pbcommon.DownloadResp.ToolInfo.version', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='author', full_name='pbcommon.DownloadResp.ToolInfo.author', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=702,
  serialized_end=798,
)

_DOWNLOADRESP = _descriptor.Descriptor(
  name='DownloadResp',
  full_name='pbcommon.DownloadResp',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='isExist', full_name='pbcommon.DownloadResp.isExist', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='url', full_name='pbcommon.DownloadResp.url', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='totalSize', full_name='pbcommon.DownloadResp.totalSize', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='toolInfo', full_name='pbcommon.DownloadResp.toolInfo', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_DOWNLOADRESP_TOOLINFO, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=586,
  serialized_end=798,
)


_UPDATEREQ = _descriptor.Descriptor(
  name='UpdateReq',
  full_name='pbcommon.UpdateReq',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='uid', full_name='pbcommon.UpdateReq.uid', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='key', full_name='pbcommon.UpdateReq.key', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='version', full_name='pbcommon.UpdateReq.version', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='commonVersion', full_name='pbcommon.UpdateReq.commonVersion', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=800,
  serialized_end=877,
)


_UPDATERESP = _descriptor.Descriptor(
  name='UpdateResp',
  full_name='pbcommon.UpdateResp',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='isUpToDate', full_name='pbcommon.UpdateResp.isUpToDate', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='updateInfo', full_name='pbcommon.UpdateResp.updateInfo', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=879,
  serialized_end=955,
)


_COMMENTREQ = _descriptor.Descriptor(
  name='CommentReq',
  full_name='pbcommon.CommentReq',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='uid', full_name='pbcommon.CommentReq.uid', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='key', full_name='pbcommon.CommentReq.key', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='version', full_name='pbcommon.CommentReq.version', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='commonVersion', full_name='pbcommon.CommentReq.commonVersion', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='score', full_name='pbcommon.CommentReq.score', index=4,
      number=5, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='content', full_name='pbcommon.CommentReq.content', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=957,
  serialized_end=1067,
)


_COLLECTREQ = _descriptor.Descriptor(
  name='CollectReq',
  full_name='pbcommon.CollectReq',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='uid', full_name='pbcommon.CollectReq.uid', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='key', full_name='pbcommon.CollectReq.key', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='version', full_name='pbcommon.CollectReq.version', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='commonVersion', full_name='pbcommon.CollectReq.commonVersion', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1069,
  serialized_end=1147,
)

_LOGINRESP.fields_by_name['userInfo'].message_type = _USERINFO
_DOWNLOADRESP_TOOLINFO.containing_type = _DOWNLOADRESP
_DOWNLOADRESP.fields_by_name['toolInfo'].message_type = _DOWNLOADRESP_TOOLINFO
_UPDATERESP.fields_by_name['updateInfo'].message_type = _DOWNLOADRESP
DESCRIPTOR.message_types_by_name['Req'] = _REQ
DESCRIPTOR.message_types_by_name['Resp'] = _RESP
DESCRIPTOR.message_types_by_name['LoginReq'] = _LOGINREQ
DESCRIPTOR.message_types_by_name['UserInfo'] = _USERINFO
DESCRIPTOR.message_types_by_name['LoginResp'] = _LOGINRESP
DESCRIPTOR.message_types_by_name['RegisterReq'] = _REGISTERREQ
DESCRIPTOR.message_types_by_name['UploadReq'] = _UPLOADREQ
DESCRIPTOR.message_types_by_name['UploadResp'] = _UPLOADRESP
DESCRIPTOR.message_types_by_name['DownloadReq'] = _DOWNLOADREQ
DESCRIPTOR.message_types_by_name['DownloadResp'] = _DOWNLOADRESP
DESCRIPTOR.message_types_by_name['UpdateReq'] = _UPDATEREQ
DESCRIPTOR.message_types_by_name['UpdateResp'] = _UPDATERESP
DESCRIPTOR.message_types_by_name['CommentReq'] = _COMMENTREQ
DESCRIPTOR.message_types_by_name['CollectReq'] = _COLLECTREQ
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Req = _reflection.GeneratedProtocolMessageType('Req', (_message.Message,), dict(
  DESCRIPTOR = _REQ,
  __module__ = 'proto.common_pb2'
  # @@protoc_insertion_point(class_scope:pbcommon.Req)
  ))
_sym_db.RegisterMessage(Req)

Resp = _reflection.GeneratedProtocolMessageType('Resp', (_message.Message,), dict(
  DESCRIPTOR = _RESP,
  __module__ = 'proto.common_pb2'
  # @@protoc_insertion_point(class_scope:pbcommon.Resp)
  ))
_sym_db.RegisterMessage(Resp)

LoginReq = _reflection.GeneratedProtocolMessageType('LoginReq', (_message.Message,), dict(
  DESCRIPTOR = _LOGINREQ,
  __module__ = 'proto.common_pb2'
  # @@protoc_insertion_point(class_scope:pbcommon.LoginReq)
  ))
_sym_db.RegisterMessage(LoginReq)

UserInfo = _reflection.GeneratedProtocolMessageType('UserInfo', (_message.Message,), dict(
  DESCRIPTOR = _USERINFO,
  __module__ = 'proto.common_pb2'
  # @@protoc_insertion_point(class_scope:pbcommon.UserInfo)
  ))
_sym_db.RegisterMessage(UserInfo)

LoginResp = _reflection.GeneratedProtocolMessageType('LoginResp', (_message.Message,), dict(
  DESCRIPTOR = _LOGINRESP,
  __module__ = 'proto.common_pb2'
  # @@protoc_insertion_point(class_scope:pbcommon.LoginResp)
  ))
_sym_db.RegisterMessage(LoginResp)

RegisterReq = _reflection.GeneratedProtocolMessageType('RegisterReq', (_message.Message,), dict(
  DESCRIPTOR = _REGISTERREQ,
  __module__ = 'proto.common_pb2'
  # @@protoc_insertion_point(class_scope:pbcommon.RegisterReq)
  ))
_sym_db.RegisterMessage(RegisterReq)

UploadReq = _reflection.GeneratedProtocolMessageType('UploadReq', (_message.Message,), dict(
  DESCRIPTOR = _UPLOADREQ,
  __module__ = 'proto.common_pb2'
  # @@protoc_insertion_point(class_scope:pbcommon.UploadReq)
  ))
_sym_db.RegisterMessage(UploadReq)

UploadResp = _reflection.GeneratedProtocolMessageType('UploadResp', (_message.Message,), dict(
  DESCRIPTOR = _UPLOADRESP,
  __module__ = 'proto.common_pb2'
  # @@protoc_insertion_point(class_scope:pbcommon.UploadResp)
  ))
_sym_db.RegisterMessage(UploadResp)

DownloadReq = _reflection.GeneratedProtocolMessageType('DownloadReq', (_message.Message,), dict(
  DESCRIPTOR = _DOWNLOADREQ,
  __module__ = 'proto.common_pb2'
  # @@protoc_insertion_point(class_scope:pbcommon.DownloadReq)
  ))
_sym_db.RegisterMessage(DownloadReq)

DownloadResp = _reflection.GeneratedProtocolMessageType('DownloadResp', (_message.Message,), dict(

  ToolInfo = _reflection.GeneratedProtocolMessageType('ToolInfo', (_message.Message,), dict(
    DESCRIPTOR = _DOWNLOADRESP_TOOLINFO,
    __module__ = 'proto.common_pb2'
    # @@protoc_insertion_point(class_scope:pbcommon.DownloadResp.ToolInfo)
    ))
  ,
  DESCRIPTOR = _DOWNLOADRESP,
  __module__ = 'proto.common_pb2'
  # @@protoc_insertion_point(class_scope:pbcommon.DownloadResp)
  ))
_sym_db.RegisterMessage(DownloadResp)
_sym_db.RegisterMessage(DownloadResp.ToolInfo)

UpdateReq = _reflection.GeneratedProtocolMessageType('UpdateReq', (_message.Message,), dict(
  DESCRIPTOR = _UPDATEREQ,
  __module__ = 'proto.common_pb2'
  # @@protoc_insertion_point(class_scope:pbcommon.UpdateReq)
  ))
_sym_db.RegisterMessage(UpdateReq)

UpdateResp = _reflection.GeneratedProtocolMessageType('UpdateResp', (_message.Message,), dict(
  DESCRIPTOR = _UPDATERESP,
  __module__ = 'proto.common_pb2'
  # @@protoc_insertion_point(class_scope:pbcommon.UpdateResp)
  ))
_sym_db.RegisterMessage(UpdateResp)

CommentReq = _reflection.GeneratedProtocolMessageType('CommentReq', (_message.Message,), dict(
  DESCRIPTOR = _COMMENTREQ,
  __module__ = 'proto.common_pb2'
  # @@protoc_insertion_point(class_scope:pbcommon.CommentReq)
  ))
_sym_db.RegisterMessage(CommentReq)

CollectReq = _reflection.GeneratedProtocolMessageType('CollectReq', (_message.Message,), dict(
  DESCRIPTOR = _COLLECTREQ,
  __module__ = 'proto.common_pb2'
  # @@protoc_insertion_point(class_scope:pbcommon.CollectReq)
  ))
_sym_db.RegisterMessage(CollectReq)



_COMMON = _descriptor.ServiceDescriptor(
  name='Common',
  full_name='pbcommon.Common',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=1150,
  serialized_end=1613,
  methods=[
  _descriptor.MethodDescriptor(
    name='Request',
    full_name='pbcommon.Common.Request',
    index=0,
    containing_service=None,
    input_type=_REQ,
    output_type=_RESP,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='Login',
    full_name='pbcommon.Common.Login',
    index=1,
    containing_service=None,
    input_type=_LOGINREQ,
    output_type=_LOGINRESP,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='Register',
    full_name='pbcommon.Common.Register',
    index=2,
    containing_service=None,
    input_type=_REGISTERREQ,
    output_type=_RESP,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='Upload',
    full_name='pbcommon.Common.Upload',
    index=3,
    containing_service=None,
    input_type=_UPLOADREQ,
    output_type=_UPLOADRESP,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='Uploaded',
    full_name='pbcommon.Common.Uploaded',
    index=4,
    containing_service=None,
    input_type=_UPLOADREQ,
    output_type=_RESP,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='Download',
    full_name='pbcommon.Common.Download',
    index=5,
    containing_service=None,
    input_type=_DOWNLOADREQ,
    output_type=_DOWNLOADRESP,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='Update',
    full_name='pbcommon.Common.Update',
    index=6,
    containing_service=None,
    input_type=_UPDATEREQ,
    output_type=_UPDATERESP,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='Comment',
    full_name='pbcommon.Common.Comment',
    index=7,
    containing_service=None,
    input_type=_COMMENTREQ,
    output_type=_RESP,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='Collect',
    full_name='pbcommon.Common.Collect',
    index=8,
    containing_service=None,
    input_type=_COLLECTREQ,
    output_type=_RESP,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_COMMON)

DESCRIPTOR.services_by_name['Common'] = _COMMON

# @@protoc_insertion_point(module_scope)

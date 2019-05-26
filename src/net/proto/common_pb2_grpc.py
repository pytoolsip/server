# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from net.proto import common_pb2 as proto_dot_common__pb2


class CommonStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.Request = channel.unary_unary(
        '/pbcommon.Common/Request',
        request_serializer=proto_dot_common__pb2.Req.SerializeToString,
        response_deserializer=proto_dot_common__pb2.Resp.FromString,
        )
    self.Login = channel.unary_unary(
        '/pbcommon.Common/Login',
        request_serializer=proto_dot_common__pb2.LoginReq.SerializeToString,
        response_deserializer=proto_dot_common__pb2.LoginResp.FromString,
        )
    self.Register = channel.unary_unary(
        '/pbcommon.Common/Register',
        request_serializer=proto_dot_common__pb2.RegisterReq.SerializeToString,
        response_deserializer=proto_dot_common__pb2.Resp.FromString,
        )
    self.Upload = channel.unary_unary(
        '/pbcommon.Common/Upload',
        request_serializer=proto_dot_common__pb2.UploadReq.SerializeToString,
        response_deserializer=proto_dot_common__pb2.UploadResp.FromString,
        )
    self.Uploaded = channel.unary_unary(
        '/pbcommon.Common/Uploaded',
        request_serializer=proto_dot_common__pb2.UploadReq.SerializeToString,
        response_deserializer=proto_dot_common__pb2.Resp.FromString,
        )
    self.Download = channel.unary_unary(
        '/pbcommon.Common/Download',
        request_serializer=proto_dot_common__pb2.DownloadReq.SerializeToString,
        response_deserializer=proto_dot_common__pb2.DownloadResp.FromString,
        )
    self.Update = channel.unary_unary(
        '/pbcommon.Common/Update',
        request_serializer=proto_dot_common__pb2.UpdateReq.SerializeToString,
        response_deserializer=proto_dot_common__pb2.UpdateResp.FromString,
        )
    self.Comment = channel.unary_unary(
        '/pbcommon.Common/Comment',
        request_serializer=proto_dot_common__pb2.CommentReq.SerializeToString,
        response_deserializer=proto_dot_common__pb2.Resp.FromString,
        )
    self.Collect = channel.unary_unary(
        '/pbcommon.Common/Collect',
        request_serializer=proto_dot_common__pb2.CollectReq.SerializeToString,
        response_deserializer=proto_dot_common__pb2.Resp.FromString,
        )
    self.UpdateIP = channel.unary_unary(
        '/pbcommon.Common/UpdateIP',
        request_serializer=proto_dot_common__pb2.UpdateIPReq.SerializeToString,
        response_deserializer=proto_dot_common__pb2.UpdateIPResp.FromString,
        )


class CommonServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def Request(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Login(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Register(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Upload(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Uploaded(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Download(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Update(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Comment(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Collect(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def UpdateIP(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_CommonServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'Request': grpc.unary_unary_rpc_method_handler(
          servicer.Request,
          request_deserializer=proto_dot_common__pb2.Req.FromString,
          response_serializer=proto_dot_common__pb2.Resp.SerializeToString,
      ),
      'Login': grpc.unary_unary_rpc_method_handler(
          servicer.Login,
          request_deserializer=proto_dot_common__pb2.LoginReq.FromString,
          response_serializer=proto_dot_common__pb2.LoginResp.SerializeToString,
      ),
      'Register': grpc.unary_unary_rpc_method_handler(
          servicer.Register,
          request_deserializer=proto_dot_common__pb2.RegisterReq.FromString,
          response_serializer=proto_dot_common__pb2.Resp.SerializeToString,
      ),
      'Upload': grpc.unary_unary_rpc_method_handler(
          servicer.Upload,
          request_deserializer=proto_dot_common__pb2.UploadReq.FromString,
          response_serializer=proto_dot_common__pb2.UploadResp.SerializeToString,
      ),
      'Uploaded': grpc.unary_unary_rpc_method_handler(
          servicer.Uploaded,
          request_deserializer=proto_dot_common__pb2.UploadReq.FromString,
          response_serializer=proto_dot_common__pb2.Resp.SerializeToString,
      ),
      'Download': grpc.unary_unary_rpc_method_handler(
          servicer.Download,
          request_deserializer=proto_dot_common__pb2.DownloadReq.FromString,
          response_serializer=proto_dot_common__pb2.DownloadResp.SerializeToString,
      ),
      'Update': grpc.unary_unary_rpc_method_handler(
          servicer.Update,
          request_deserializer=proto_dot_common__pb2.UpdateReq.FromString,
          response_serializer=proto_dot_common__pb2.UpdateResp.SerializeToString,
      ),
      'Comment': grpc.unary_unary_rpc_method_handler(
          servicer.Comment,
          request_deserializer=proto_dot_common__pb2.CommentReq.FromString,
          response_serializer=proto_dot_common__pb2.Resp.SerializeToString,
      ),
      'Collect': grpc.unary_unary_rpc_method_handler(
          servicer.Collect,
          request_deserializer=proto_dot_common__pb2.CollectReq.FromString,
          response_serializer=proto_dot_common__pb2.Resp.SerializeToString,
      ),
      'UpdateIP': grpc.unary_unary_rpc_method_handler(
          servicer.UpdateIP,
          request_deserializer=proto_dot_common__pb2.UpdateIPReq.FromString,
          response_serializer=proto_dot_common__pb2.UpdateIPResp.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'pbcommon.Common', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))

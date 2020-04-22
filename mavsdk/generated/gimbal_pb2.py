# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: gimbal.proto

from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='gimbal.proto',
  package='mavsdk.rpc.gimbal',
  syntax='proto3',
  serialized_options=b'\n\020io.mavsdk.gimbalB\013GimbalProto',
  serialized_pb=b'\n\x0cgimbal.proto\x12\x11mavsdk.rpc.gimbal\";\n\x15SetPitchAndYawRequest\x12\x11\n\tpitch_deg\x18\x01 \x01(\x02\x12\x0f\n\x07yaw_deg\x18\x02 \x01(\x02\"P\n\x16SetPitchAndYawResponse\x12\x36\n\rgimbal_result\x18\x01 \x01(\x0b\x32\x1f.mavsdk.rpc.gimbal.GimbalResult\"D\n\x0eSetModeRequest\x12\x32\n\x0bgimbal_mode\x18\x01 \x01(\x0e\x32\x1d.mavsdk.rpc.gimbal.GimbalMode\"I\n\x0fSetModeResponse\x12\x36\n\rgimbal_result\x18\x01 \x01(\x0b\x32\x1f.mavsdk.rpc.gimbal.GimbalResult\"\x96\x01\n\x0cGimbalResult\x12\x36\n\x06result\x18\x01 \x01(\x0e\x32&.mavsdk.rpc.gimbal.GimbalResult.Result\x12\x12\n\nresult_str\x18\x02 \x01(\t\":\n\x06Result\x12\x0b\n\x07UNKNOWN\x10\x00\x12\x0b\n\x07SUCCESS\x10\x01\x12\t\n\x05\x45RROR\x10\x02\x12\x0b\n\x07TIMEOUT\x10\x03**\n\nGimbalMode\x12\x0e\n\nYAW_FOLLOW\x10\x00\x12\x0c\n\x08YAW_LOCK\x10\x01\x32\xcc\x01\n\rGimbalService\x12g\n\x0eSetPitchAndYaw\x12(.mavsdk.rpc.gimbal.SetPitchAndYawRequest\x1a).mavsdk.rpc.gimbal.SetPitchAndYawResponse\"\x00\x12R\n\x07SetMode\x12!.mavsdk.rpc.gimbal.SetModeRequest\x1a\".mavsdk.rpc.gimbal.SetModeResponse\"\x00\x42\x1f\n\x10io.mavsdk.gimbalB\x0bGimbalProtob\x06proto3'
)

_GIMBALMODE = _descriptor.EnumDescriptor(
  name='GimbalMode',
  full_name='mavsdk.rpc.gimbal.GimbalMode',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='YAW_FOLLOW', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='YAW_LOCK', index=1, number=1,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=476,
  serialized_end=518,
)
_sym_db.RegisterEnumDescriptor(_GIMBALMODE)

GimbalMode = enum_type_wrapper.EnumTypeWrapper(_GIMBALMODE)
YAW_FOLLOW = 0
YAW_LOCK = 1


_GIMBALRESULT_RESULT = _descriptor.EnumDescriptor(
  name='Result',
  full_name='mavsdk.rpc.gimbal.GimbalResult.Result',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SUCCESS', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TIMEOUT', index=3, number=3,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=416,
  serialized_end=474,
)
_sym_db.RegisterEnumDescriptor(_GIMBALRESULT_RESULT)


_SETPITCHANDYAWREQUEST = _descriptor.Descriptor(
  name='SetPitchAndYawRequest',
  full_name='mavsdk.rpc.gimbal.SetPitchAndYawRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='pitch_deg', full_name='mavsdk.rpc.gimbal.SetPitchAndYawRequest.pitch_deg', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='yaw_deg', full_name='mavsdk.rpc.gimbal.SetPitchAndYawRequest.yaw_deg', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
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
  serialized_start=35,
  serialized_end=94,
)


_SETPITCHANDYAWRESPONSE = _descriptor.Descriptor(
  name='SetPitchAndYawResponse',
  full_name='mavsdk.rpc.gimbal.SetPitchAndYawResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='gimbal_result', full_name='mavsdk.rpc.gimbal.SetPitchAndYawResponse.gimbal_result', index=0,
      number=1, type=11, cpp_type=10, label=1,
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
  serialized_start=96,
  serialized_end=176,
)


_SETMODEREQUEST = _descriptor.Descriptor(
  name='SetModeRequest',
  full_name='mavsdk.rpc.gimbal.SetModeRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='gimbal_mode', full_name='mavsdk.rpc.gimbal.SetModeRequest.gimbal_mode', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=178,
  serialized_end=246,
)


_SETMODERESPONSE = _descriptor.Descriptor(
  name='SetModeResponse',
  full_name='mavsdk.rpc.gimbal.SetModeResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='gimbal_result', full_name='mavsdk.rpc.gimbal.SetModeResponse.gimbal_result', index=0,
      number=1, type=11, cpp_type=10, label=1,
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
  serialized_start=248,
  serialized_end=321,
)


_GIMBALRESULT = _descriptor.Descriptor(
  name='GimbalResult',
  full_name='mavsdk.rpc.gimbal.GimbalResult',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='result', full_name='mavsdk.rpc.gimbal.GimbalResult.result', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='result_str', full_name='mavsdk.rpc.gimbal.GimbalResult.result_str', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _GIMBALRESULT_RESULT,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=324,
  serialized_end=474,
)

_SETPITCHANDYAWRESPONSE.fields_by_name['gimbal_result'].message_type = _GIMBALRESULT
_SETMODEREQUEST.fields_by_name['gimbal_mode'].enum_type = _GIMBALMODE
_SETMODERESPONSE.fields_by_name['gimbal_result'].message_type = _GIMBALRESULT
_GIMBALRESULT.fields_by_name['result'].enum_type = _GIMBALRESULT_RESULT
_GIMBALRESULT_RESULT.containing_type = _GIMBALRESULT
DESCRIPTOR.message_types_by_name['SetPitchAndYawRequest'] = _SETPITCHANDYAWREQUEST
DESCRIPTOR.message_types_by_name['SetPitchAndYawResponse'] = _SETPITCHANDYAWRESPONSE
DESCRIPTOR.message_types_by_name['SetModeRequest'] = _SETMODEREQUEST
DESCRIPTOR.message_types_by_name['SetModeResponse'] = _SETMODERESPONSE
DESCRIPTOR.message_types_by_name['GimbalResult'] = _GIMBALRESULT
DESCRIPTOR.enum_types_by_name['GimbalMode'] = _GIMBALMODE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

SetPitchAndYawRequest = _reflection.GeneratedProtocolMessageType('SetPitchAndYawRequest', (_message.Message,), {
  'DESCRIPTOR' : _SETPITCHANDYAWREQUEST,
  '__module__' : 'gimbal_pb2'
  # @@protoc_insertion_point(class_scope:mavsdk.rpc.gimbal.SetPitchAndYawRequest)
  })
_sym_db.RegisterMessage(SetPitchAndYawRequest)

SetPitchAndYawResponse = _reflection.GeneratedProtocolMessageType('SetPitchAndYawResponse', (_message.Message,), {
  'DESCRIPTOR' : _SETPITCHANDYAWRESPONSE,
  '__module__' : 'gimbal_pb2'
  # @@protoc_insertion_point(class_scope:mavsdk.rpc.gimbal.SetPitchAndYawResponse)
  })
_sym_db.RegisterMessage(SetPitchAndYawResponse)

SetModeRequest = _reflection.GeneratedProtocolMessageType('SetModeRequest', (_message.Message,), {
  'DESCRIPTOR' : _SETMODEREQUEST,
  '__module__' : 'gimbal_pb2'
  # @@protoc_insertion_point(class_scope:mavsdk.rpc.gimbal.SetModeRequest)
  })
_sym_db.RegisterMessage(SetModeRequest)

SetModeResponse = _reflection.GeneratedProtocolMessageType('SetModeResponse', (_message.Message,), {
  'DESCRIPTOR' : _SETMODERESPONSE,
  '__module__' : 'gimbal_pb2'
  # @@protoc_insertion_point(class_scope:mavsdk.rpc.gimbal.SetModeResponse)
  })
_sym_db.RegisterMessage(SetModeResponse)

GimbalResult = _reflection.GeneratedProtocolMessageType('GimbalResult', (_message.Message,), {
  'DESCRIPTOR' : _GIMBALRESULT,
  '__module__' : 'gimbal_pb2'
  # @@protoc_insertion_point(class_scope:mavsdk.rpc.gimbal.GimbalResult)
  })
_sym_db.RegisterMessage(GimbalResult)


DESCRIPTOR._options = None

_GIMBALSERVICE = _descriptor.ServiceDescriptor(
  name='GimbalService',
  full_name='mavsdk.rpc.gimbal.GimbalService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=521,
  serialized_end=725,
  methods=[
  _descriptor.MethodDescriptor(
    name='SetPitchAndYaw',
    full_name='mavsdk.rpc.gimbal.GimbalService.SetPitchAndYaw',
    index=0,
    containing_service=None,
    input_type=_SETPITCHANDYAWREQUEST,
    output_type=_SETPITCHANDYAWRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='SetMode',
    full_name='mavsdk.rpc.gimbal.GimbalService.SetMode',
    index=1,
    containing_service=None,
    input_type=_SETMODEREQUEST,
    output_type=_SETMODERESPONSE,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_GIMBALSERVICE)

DESCRIPTOR.services_by_name['GimbalService'] = _GIMBALSERVICE

# @@protoc_insertion_point(module_scope)

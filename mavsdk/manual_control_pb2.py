# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: manual_control/manual_control.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from . import mavsdk_options_pb2 as mavsdk__options__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='manual_control/manual_control.proto',
  package='mavsdk.rpc.manual_control',
  syntax='proto3',
  serialized_options=b'\n\030io.mavsdk.manual_controlB\022ManualControlProto',
  serialized_pb=b'\n#manual_control/manual_control.proto\x12\x19mavsdk.rpc.manual_control\x1a\x14mavsdk_options.proto\"\x1d\n\x1bStartPositionControlRequest\"m\n\x1cStartPositionControlResponse\x12M\n\x15manual_control_result\x18\x01 \x01(\x0b\x32..mavsdk.rpc.manual_control.ManualControlResult\"\x1d\n\x1bStartAltitudeControlRequest\"m\n\x1cStartAltitudeControlResponse\x12M\n\x15manual_control_result\x18\x01 \x01(\x0b\x32..mavsdk.rpc.manual_control.ManualControlResult\"J\n\x1cSetManualControlInputRequest\x12\t\n\x01x\x18\x01 \x01(\x02\x12\t\n\x01y\x18\x02 \x01(\x02\x12\t\n\x01z\x18\x03 \x01(\x02\x12\t\n\x01r\x18\x04 \x01(\x02\"n\n\x1dSetManualControlInputResponse\x12M\n\x15manual_control_result\x18\x01 \x01(\x0b\x32..mavsdk.rpc.manual_control.ManualControlResult\"\xb5\x02\n\x13ManualControlResult\x12\x45\n\x06result\x18\x01 \x01(\x0e\x32\x35.mavsdk.rpc.manual_control.ManualControlResult.Result\x12\x12\n\nresult_str\x18\x02 \x01(\t\"\xc2\x01\n\x06Result\x12\x12\n\x0eRESULT_UNKNOWN\x10\x00\x12\x12\n\x0eRESULT_SUCCESS\x10\x01\x12\x14\n\x10RESULT_NO_SYSTEM\x10\x02\x12\x1b\n\x17RESULT_CONNECTION_ERROR\x10\x03\x12\x0f\n\x0bRESULT_BUSY\x10\x04\x12\x19\n\x15RESULT_COMMAND_DENIED\x10\x05\x12\x12\n\x0eRESULT_TIMEOUT\x10\x06\x12\x1d\n\x19RESULT_INPUT_OUT_OF_RANGE\x10\x07\x32\xc1\x03\n\x14ManualControlService\x12\x89\x01\n\x14StartPositionControl\x12\x36.mavsdk.rpc.manual_control.StartPositionControlRequest\x1a\x37.mavsdk.rpc.manual_control.StartPositionControlResponse\"\x00\x12\x89\x01\n\x14StartAltitudeControl\x12\x36.mavsdk.rpc.manual_control.StartAltitudeControlRequest\x1a\x37.mavsdk.rpc.manual_control.StartAltitudeControlResponse\"\x00\x12\x90\x01\n\x15SetManualControlInput\x12\x37.mavsdk.rpc.manual_control.SetManualControlInputRequest\x1a\x38.mavsdk.rpc.manual_control.SetManualControlInputResponse\"\x04\x80\xb5\x18\x01\x42.\n\x18io.mavsdk.manual_controlB\x12ManualControlProtob\x06proto3'
  ,
  dependencies=[mavsdk__options__pb2.DESCRIPTOR,])



_MANUALCONTROLRESULT_RESULT = _descriptor.EnumDescriptor(
  name='Result',
  full_name='mavsdk.rpc.manual_control.ManualControlResult.Result',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='RESULT_UNKNOWN', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='RESULT_SUCCESS', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='RESULT_NO_SYSTEM', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='RESULT_CONNECTION_ERROR', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='RESULT_BUSY', index=4, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='RESULT_COMMAND_DENIED', index=5, number=5,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='RESULT_TIMEOUT', index=6, number=6,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='RESULT_INPUT_OUT_OF_RANGE', index=7, number=7,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=676,
  serialized_end=870,
)
_sym_db.RegisterEnumDescriptor(_MANUALCONTROLRESULT_RESULT)


_STARTPOSITIONCONTROLREQUEST = _descriptor.Descriptor(
  name='StartPositionControlRequest',
  full_name='mavsdk.rpc.manual_control.StartPositionControlRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
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
  serialized_start=88,
  serialized_end=117,
)


_STARTPOSITIONCONTROLRESPONSE = _descriptor.Descriptor(
  name='StartPositionControlResponse',
  full_name='mavsdk.rpc.manual_control.StartPositionControlResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='manual_control_result', full_name='mavsdk.rpc.manual_control.StartPositionControlResponse.manual_control_result', index=0,
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
  serialized_start=119,
  serialized_end=228,
)


_STARTALTITUDECONTROLREQUEST = _descriptor.Descriptor(
  name='StartAltitudeControlRequest',
  full_name='mavsdk.rpc.manual_control.StartAltitudeControlRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
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
  serialized_start=230,
  serialized_end=259,
)


_STARTALTITUDECONTROLRESPONSE = _descriptor.Descriptor(
  name='StartAltitudeControlResponse',
  full_name='mavsdk.rpc.manual_control.StartAltitudeControlResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='manual_control_result', full_name='mavsdk.rpc.manual_control.StartAltitudeControlResponse.manual_control_result', index=0,
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
  serialized_start=261,
  serialized_end=370,
)


_SETMANUALCONTROLINPUTREQUEST = _descriptor.Descriptor(
  name='SetManualControlInputRequest',
  full_name='mavsdk.rpc.manual_control.SetManualControlInputRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='x', full_name='mavsdk.rpc.manual_control.SetManualControlInputRequest.x', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='y', full_name='mavsdk.rpc.manual_control.SetManualControlInputRequest.y', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='z', full_name='mavsdk.rpc.manual_control.SetManualControlInputRequest.z', index=2,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='r', full_name='mavsdk.rpc.manual_control.SetManualControlInputRequest.r', index=3,
      number=4, type=2, cpp_type=6, label=1,
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
  serialized_start=372,
  serialized_end=446,
)


_SETMANUALCONTROLINPUTRESPONSE = _descriptor.Descriptor(
  name='SetManualControlInputResponse',
  full_name='mavsdk.rpc.manual_control.SetManualControlInputResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='manual_control_result', full_name='mavsdk.rpc.manual_control.SetManualControlInputResponse.manual_control_result', index=0,
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
  serialized_start=448,
  serialized_end=558,
)


_MANUALCONTROLRESULT = _descriptor.Descriptor(
  name='ManualControlResult',
  full_name='mavsdk.rpc.manual_control.ManualControlResult',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='result', full_name='mavsdk.rpc.manual_control.ManualControlResult.result', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='result_str', full_name='mavsdk.rpc.manual_control.ManualControlResult.result_str', index=1,
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
    _MANUALCONTROLRESULT_RESULT,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=561,
  serialized_end=870,
)

_STARTPOSITIONCONTROLRESPONSE.fields_by_name['manual_control_result'].message_type = _MANUALCONTROLRESULT
_STARTALTITUDECONTROLRESPONSE.fields_by_name['manual_control_result'].message_type = _MANUALCONTROLRESULT
_SETMANUALCONTROLINPUTRESPONSE.fields_by_name['manual_control_result'].message_type = _MANUALCONTROLRESULT
_MANUALCONTROLRESULT.fields_by_name['result'].enum_type = _MANUALCONTROLRESULT_RESULT
_MANUALCONTROLRESULT_RESULT.containing_type = _MANUALCONTROLRESULT
DESCRIPTOR.message_types_by_name['StartPositionControlRequest'] = _STARTPOSITIONCONTROLREQUEST
DESCRIPTOR.message_types_by_name['StartPositionControlResponse'] = _STARTPOSITIONCONTROLRESPONSE
DESCRIPTOR.message_types_by_name['StartAltitudeControlRequest'] = _STARTALTITUDECONTROLREQUEST
DESCRIPTOR.message_types_by_name['StartAltitudeControlResponse'] = _STARTALTITUDECONTROLRESPONSE
DESCRIPTOR.message_types_by_name['SetManualControlInputRequest'] = _SETMANUALCONTROLINPUTREQUEST
DESCRIPTOR.message_types_by_name['SetManualControlInputResponse'] = _SETMANUALCONTROLINPUTRESPONSE
DESCRIPTOR.message_types_by_name['ManualControlResult'] = _MANUALCONTROLRESULT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

StartPositionControlRequest = _reflection.GeneratedProtocolMessageType('StartPositionControlRequest', (_message.Message,), {
  'DESCRIPTOR' : _STARTPOSITIONCONTROLREQUEST,
  '__module__' : 'manual_control.manual_control_pb2'
  # @@protoc_insertion_point(class_scope:mavsdk.rpc.manual_control.StartPositionControlRequest)
  })
_sym_db.RegisterMessage(StartPositionControlRequest)

StartPositionControlResponse = _reflection.GeneratedProtocolMessageType('StartPositionControlResponse', (_message.Message,), {
  'DESCRIPTOR' : _STARTPOSITIONCONTROLRESPONSE,
  '__module__' : 'manual_control.manual_control_pb2'
  # @@protoc_insertion_point(class_scope:mavsdk.rpc.manual_control.StartPositionControlResponse)
  })
_sym_db.RegisterMessage(StartPositionControlResponse)

StartAltitudeControlRequest = _reflection.GeneratedProtocolMessageType('StartAltitudeControlRequest', (_message.Message,), {
  'DESCRIPTOR' : _STARTALTITUDECONTROLREQUEST,
  '__module__' : 'manual_control.manual_control_pb2'
  # @@protoc_insertion_point(class_scope:mavsdk.rpc.manual_control.StartAltitudeControlRequest)
  })
_sym_db.RegisterMessage(StartAltitudeControlRequest)

StartAltitudeControlResponse = _reflection.GeneratedProtocolMessageType('StartAltitudeControlResponse', (_message.Message,), {
  'DESCRIPTOR' : _STARTALTITUDECONTROLRESPONSE,
  '__module__' : 'manual_control.manual_control_pb2'
  # @@protoc_insertion_point(class_scope:mavsdk.rpc.manual_control.StartAltitudeControlResponse)
  })
_sym_db.RegisterMessage(StartAltitudeControlResponse)

SetManualControlInputRequest = _reflection.GeneratedProtocolMessageType('SetManualControlInputRequest', (_message.Message,), {
  'DESCRIPTOR' : _SETMANUALCONTROLINPUTREQUEST,
  '__module__' : 'manual_control.manual_control_pb2'
  # @@protoc_insertion_point(class_scope:mavsdk.rpc.manual_control.SetManualControlInputRequest)
  })
_sym_db.RegisterMessage(SetManualControlInputRequest)

SetManualControlInputResponse = _reflection.GeneratedProtocolMessageType('SetManualControlInputResponse', (_message.Message,), {
  'DESCRIPTOR' : _SETMANUALCONTROLINPUTRESPONSE,
  '__module__' : 'manual_control.manual_control_pb2'
  # @@protoc_insertion_point(class_scope:mavsdk.rpc.manual_control.SetManualControlInputResponse)
  })
_sym_db.RegisterMessage(SetManualControlInputResponse)

ManualControlResult = _reflection.GeneratedProtocolMessageType('ManualControlResult', (_message.Message,), {
  'DESCRIPTOR' : _MANUALCONTROLRESULT,
  '__module__' : 'manual_control.manual_control_pb2'
  # @@protoc_insertion_point(class_scope:mavsdk.rpc.manual_control.ManualControlResult)
  })
_sym_db.RegisterMessage(ManualControlResult)


DESCRIPTOR._options = None

_MANUALCONTROLSERVICE = _descriptor.ServiceDescriptor(
  name='ManualControlService',
  full_name='mavsdk.rpc.manual_control.ManualControlService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=873,
  serialized_end=1322,
  methods=[
  _descriptor.MethodDescriptor(
    name='StartPositionControl',
    full_name='mavsdk.rpc.manual_control.ManualControlService.StartPositionControl',
    index=0,
    containing_service=None,
    input_type=_STARTPOSITIONCONTROLREQUEST,
    output_type=_STARTPOSITIONCONTROLRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='StartAltitudeControl',
    full_name='mavsdk.rpc.manual_control.ManualControlService.StartAltitudeControl',
    index=1,
    containing_service=None,
    input_type=_STARTALTITUDECONTROLREQUEST,
    output_type=_STARTALTITUDECONTROLRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='SetManualControlInput',
    full_name='mavsdk.rpc.manual_control.ManualControlService.SetManualControlInput',
    index=2,
    containing_service=None,
    input_type=_SETMANUALCONTROLINPUTREQUEST,
    output_type=_SETMANUALCONTROLINPUTRESPONSE,
    serialized_options=b'\200\265\030\001',
  ),
])
_sym_db.RegisterServiceDescriptor(_MANUALCONTROLSERVICE)

DESCRIPTOR.services_by_name['ManualControlService'] = _MANUALCONTROLSERVICE

# @@protoc_insertion_point(module_scope)

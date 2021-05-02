# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: srv6_manager.proto

from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import commons_pb2 as commons__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='srv6_manager.proto',
  package='srv6_manager',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=b'\n\x12srv6_manager.proto\x12\x0csrv6_manager\x1a\rcommons.proto\"\xce\x01\n\x12SRv6ManagerRequest\x12\x38\n\x11srv6_path_request\x18\x01 \x01(\x0b\x32\x1d.srv6_manager.SRv6PathRequest\x12@\n\x15srv6_behavior_request\x18\x02 \x01(\x0b\x32!.srv6_manager.SRv6BehaviorRequest\x12<\n\x13srv6_policy_request\x18\x03 \x01(\x0b\x32\x1f.srv6_manager.SRv6PolicyRequest\"\xbf\x01\n\x10SRv6ManagerReply\x12)\n\x06status\x18\x01 \x01(\x0e\x32\x19.srv6_services.StatusCode\x12%\n\x05paths\x18\x02 \x03(\x0b\x32\x16.srv6_manager.SRv6Path\x12-\n\tbehaviors\x18\x03 \x03(\x0b\x32\x1a.srv6_manager.SRv6Behavior\x12*\n\x08policies\x18\x04 \x03(\x0b\x32\x18.srv6_manager.SRv6Policy\"e\n\x0fSRv6PathRequest\x12%\n\x05paths\x18\x01 \x03(\x0b\x32\x16.srv6_manager.SRv6Path\x12+\n\nfwd_engine\x18\x02 \x01(\x0e\x32\x17.srv6_manager.FwdEngine\"l\n\x11SRv6PolicyRequest\x12*\n\x08policies\x18\x01 \x03(\x0b\x32\x18.srv6_manager.SRv6Policy\x12+\n\nfwd_engine\x18\x02 \x01(\x0e\x32\x17.srv6_manager.FwdEngine\"\xc9\x01\n\x08SRv6Path\x12\x13\n\x0b\x64\x65stination\x18\x01 \x01(\t\x12\x33\n\x07sr_path\x18\x02 \x03(\x0b\x32\".srv6_manager.SRv6Path.SRv6Segment\x12\x11\n\tencapmode\x18\x03 \x01(\t\x12\x0e\n\x06\x64\x65vice\x18\x04 \x01(\t\x12\r\n\x05table\x18\x05 \x01(\x05\x12\x0e\n\x06metric\x18\x06 \x01(\x05\x12\x11\n\tbsid_addr\x18\x07 \x01(\t\x1a\x1e\n\x0bSRv6Segment\x12\x0f\n\x07segment\x18\x01 \x01(\t\"\x95\x01\n\nSRv6Policy\x12\x11\n\tbsid_addr\x18\x01 \x01(\t\x12\x35\n\x07sr_path\x18\x02 \x03(\x0b\x32$.srv6_manager.SRv6Policy.SRv6Segment\x12\r\n\x05table\x18\x05 \x01(\x05\x12\x0e\n\x06metric\x18\x06 \x01(\x05\x1a\x1e\n\x0bSRv6Segment\x12\x0f\n\x07segment\x18\x01 \x01(\t\"q\n\x13SRv6BehaviorRequest\x12-\n\tbehaviors\x18\x01 \x03(\x0b\x32\x1a.srv6_manager.SRv6Behavior\x12+\n\nfwd_engine\x18\x02 \x01(\x0e\x32\x17.srv6_manager.FwdEngine\"\xee\x01\n\x0cSRv6Behavior\x12\x0f\n\x07segment\x18\x01 \x01(\t\x12\x0e\n\x06\x61\x63tion\x18\x02 \x01(\t\x12\x0f\n\x07nexthop\x18\x03 \x01(\t\x12\x14\n\x0clookup_table\x18\x04 \x01(\x05\x12\x11\n\tinterface\x18\x05 \x01(\t\x12\x34\n\x04segs\x18\x06 \x03(\x0b\x32&.srv6_manager.SRv6Behavior.SRv6Segment\x12\x0e\n\x06\x64\x65vice\x18\x07 \x01(\t\x12\r\n\x05table\x18\x08 \x01(\x05\x12\x0e\n\x06metric\x18\t \x01(\x05\x1a\x1e\n\x0bSRv6Segment\x12\x0f\n\x07segment\x18\x01 \x01(\t*\'\n\tFwdEngine\x12\t\n\x05Linux\x10\x00\x12\x07\n\x03VPP\x10\x01\x12\x06\n\x02P4\x10\x02\x32\xc2\x02\n\x0bSRv6Manager\x12L\n\x06\x43reate\x12 .srv6_manager.SRv6ManagerRequest\x1a\x1e.srv6_manager.SRv6ManagerReply\"\x00\x12I\n\x03Get\x12 .srv6_manager.SRv6ManagerRequest\x1a\x1e.srv6_manager.SRv6ManagerReply\"\x00\x12L\n\x06Update\x12 .srv6_manager.SRv6ManagerRequest\x1a\x1e.srv6_manager.SRv6ManagerReply\"\x00\x12L\n\x06Remove\x12 .srv6_manager.SRv6ManagerRequest\x1a\x1e.srv6_manager.SRv6ManagerReply\"\x00\x62\x06proto3'
  ,
  dependencies=[commons__pb2.DESCRIPTOR,])

_FWDENGINE = _descriptor.EnumDescriptor(
  name='FwdEngine',
  full_name='srv6_manager.FwdEngine',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='Linux', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='VPP', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='P4', index=2, number=2,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1379,
  serialized_end=1418,
)
_sym_db.RegisterEnumDescriptor(_FWDENGINE)

FwdEngine = enum_type_wrapper.EnumTypeWrapper(_FWDENGINE)
Linux = 0
VPP = 1
P4 = 2



_SRV6MANAGERREQUEST = _descriptor.Descriptor(
  name='SRv6ManagerRequest',
  full_name='srv6_manager.SRv6ManagerRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='srv6_path_request', full_name='srv6_manager.SRv6ManagerRequest.srv6_path_request', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='srv6_behavior_request', full_name='srv6_manager.SRv6ManagerRequest.srv6_behavior_request', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='srv6_policy_request', full_name='srv6_manager.SRv6ManagerRequest.srv6_policy_request', index=2,
      number=3, type=11, cpp_type=10, label=1,
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
  serialized_start=52,
  serialized_end=258,
)


_SRV6MANAGERREPLY = _descriptor.Descriptor(
  name='SRv6ManagerReply',
  full_name='srv6_manager.SRv6ManagerReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='srv6_manager.SRv6ManagerReply.status', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='paths', full_name='srv6_manager.SRv6ManagerReply.paths', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='behaviors', full_name='srv6_manager.SRv6ManagerReply.behaviors', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='policies', full_name='srv6_manager.SRv6ManagerReply.policies', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_end=452,
)


_SRV6PATHREQUEST = _descriptor.Descriptor(
  name='SRv6PathRequest',
  full_name='srv6_manager.SRv6PathRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='paths', full_name='srv6_manager.SRv6PathRequest.paths', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='fwd_engine', full_name='srv6_manager.SRv6PathRequest.fwd_engine', index=1,
      number=2, type=14, cpp_type=8, label=1,
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
  serialized_start=454,
  serialized_end=555,
)


_SRV6POLICYREQUEST = _descriptor.Descriptor(
  name='SRv6PolicyRequest',
  full_name='srv6_manager.SRv6PolicyRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='policies', full_name='srv6_manager.SRv6PolicyRequest.policies', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='fwd_engine', full_name='srv6_manager.SRv6PolicyRequest.fwd_engine', index=1,
      number=2, type=14, cpp_type=8, label=1,
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
  serialized_start=557,
  serialized_end=665,
)


_SRV6PATH_SRV6SEGMENT = _descriptor.Descriptor(
  name='SRv6Segment',
  full_name='srv6_manager.SRv6Path.SRv6Segment',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='segment', full_name='srv6_manager.SRv6Path.SRv6Segment.segment', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
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
  serialized_start=839,
  serialized_end=869,
)

_SRV6PATH = _descriptor.Descriptor(
  name='SRv6Path',
  full_name='srv6_manager.SRv6Path',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='destination', full_name='srv6_manager.SRv6Path.destination', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='sr_path', full_name='srv6_manager.SRv6Path.sr_path', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='encapmode', full_name='srv6_manager.SRv6Path.encapmode', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='device', full_name='srv6_manager.SRv6Path.device', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='table', full_name='srv6_manager.SRv6Path.table', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='metric', full_name='srv6_manager.SRv6Path.metric', index=5,
      number=6, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='bsid_addr', full_name='srv6_manager.SRv6Path.bsid_addr', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_SRV6PATH_SRV6SEGMENT, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=668,
  serialized_end=869,
)


_SRV6POLICY_SRV6SEGMENT = _descriptor.Descriptor(
  name='SRv6Segment',
  full_name='srv6_manager.SRv6Policy.SRv6Segment',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='segment', full_name='srv6_manager.SRv6Policy.SRv6Segment.segment', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
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
  serialized_start=839,
  serialized_end=869,
)

_SRV6POLICY = _descriptor.Descriptor(
  name='SRv6Policy',
  full_name='srv6_manager.SRv6Policy',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='bsid_addr', full_name='srv6_manager.SRv6Policy.bsid_addr', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='sr_path', full_name='srv6_manager.SRv6Policy.sr_path', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='table', full_name='srv6_manager.SRv6Policy.table', index=2,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='metric', full_name='srv6_manager.SRv6Policy.metric', index=3,
      number=6, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_SRV6POLICY_SRV6SEGMENT, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=872,
  serialized_end=1021,
)


_SRV6BEHAVIORREQUEST = _descriptor.Descriptor(
  name='SRv6BehaviorRequest',
  full_name='srv6_manager.SRv6BehaviorRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='behaviors', full_name='srv6_manager.SRv6BehaviorRequest.behaviors', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='fwd_engine', full_name='srv6_manager.SRv6BehaviorRequest.fwd_engine', index=1,
      number=2, type=14, cpp_type=8, label=1,
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
  serialized_start=1023,
  serialized_end=1136,
)


_SRV6BEHAVIOR_SRV6SEGMENT = _descriptor.Descriptor(
  name='SRv6Segment',
  full_name='srv6_manager.SRv6Behavior.SRv6Segment',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='segment', full_name='srv6_manager.SRv6Behavior.SRv6Segment.segment', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
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
  serialized_start=839,
  serialized_end=869,
)

_SRV6BEHAVIOR = _descriptor.Descriptor(
  name='SRv6Behavior',
  full_name='srv6_manager.SRv6Behavior',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='segment', full_name='srv6_manager.SRv6Behavior.segment', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='action', full_name='srv6_manager.SRv6Behavior.action', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='nexthop', full_name='srv6_manager.SRv6Behavior.nexthop', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='lookup_table', full_name='srv6_manager.SRv6Behavior.lookup_table', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='interface', full_name='srv6_manager.SRv6Behavior.interface', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='segs', full_name='srv6_manager.SRv6Behavior.segs', index=5,
      number=6, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='device', full_name='srv6_manager.SRv6Behavior.device', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='table', full_name='srv6_manager.SRv6Behavior.table', index=7,
      number=8, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='metric', full_name='srv6_manager.SRv6Behavior.metric', index=8,
      number=9, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_SRV6BEHAVIOR_SRV6SEGMENT, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1139,
  serialized_end=1377,
)

_SRV6MANAGERREQUEST.fields_by_name['srv6_path_request'].message_type = _SRV6PATHREQUEST
_SRV6MANAGERREQUEST.fields_by_name['srv6_behavior_request'].message_type = _SRV6BEHAVIORREQUEST
_SRV6MANAGERREQUEST.fields_by_name['srv6_policy_request'].message_type = _SRV6POLICYREQUEST
_SRV6MANAGERREPLY.fields_by_name['status'].enum_type = commons__pb2._STATUSCODE
_SRV6MANAGERREPLY.fields_by_name['paths'].message_type = _SRV6PATH
_SRV6MANAGERREPLY.fields_by_name['behaviors'].message_type = _SRV6BEHAVIOR
_SRV6MANAGERREPLY.fields_by_name['policies'].message_type = _SRV6POLICY
_SRV6PATHREQUEST.fields_by_name['paths'].message_type = _SRV6PATH
_SRV6PATHREQUEST.fields_by_name['fwd_engine'].enum_type = _FWDENGINE
_SRV6POLICYREQUEST.fields_by_name['policies'].message_type = _SRV6POLICY
_SRV6POLICYREQUEST.fields_by_name['fwd_engine'].enum_type = _FWDENGINE
_SRV6PATH_SRV6SEGMENT.containing_type = _SRV6PATH
_SRV6PATH.fields_by_name['sr_path'].message_type = _SRV6PATH_SRV6SEGMENT
_SRV6POLICY_SRV6SEGMENT.containing_type = _SRV6POLICY
_SRV6POLICY.fields_by_name['sr_path'].message_type = _SRV6POLICY_SRV6SEGMENT
_SRV6BEHAVIORREQUEST.fields_by_name['behaviors'].message_type = _SRV6BEHAVIOR
_SRV6BEHAVIORREQUEST.fields_by_name['fwd_engine'].enum_type = _FWDENGINE
_SRV6BEHAVIOR_SRV6SEGMENT.containing_type = _SRV6BEHAVIOR
_SRV6BEHAVIOR.fields_by_name['segs'].message_type = _SRV6BEHAVIOR_SRV6SEGMENT
DESCRIPTOR.message_types_by_name['SRv6ManagerRequest'] = _SRV6MANAGERREQUEST
DESCRIPTOR.message_types_by_name['SRv6ManagerReply'] = _SRV6MANAGERREPLY
DESCRIPTOR.message_types_by_name['SRv6PathRequest'] = _SRV6PATHREQUEST
DESCRIPTOR.message_types_by_name['SRv6PolicyRequest'] = _SRV6POLICYREQUEST
DESCRIPTOR.message_types_by_name['SRv6Path'] = _SRV6PATH
DESCRIPTOR.message_types_by_name['SRv6Policy'] = _SRV6POLICY
DESCRIPTOR.message_types_by_name['SRv6BehaviorRequest'] = _SRV6BEHAVIORREQUEST
DESCRIPTOR.message_types_by_name['SRv6Behavior'] = _SRV6BEHAVIOR
DESCRIPTOR.enum_types_by_name['FwdEngine'] = _FWDENGINE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

SRv6ManagerRequest = _reflection.GeneratedProtocolMessageType('SRv6ManagerRequest', (_message.Message,), {
  'DESCRIPTOR' : _SRV6MANAGERREQUEST,
  '__module__' : 'srv6_manager_pb2'
  # @@protoc_insertion_point(class_scope:srv6_manager.SRv6ManagerRequest)
  })
_sym_db.RegisterMessage(SRv6ManagerRequest)

SRv6ManagerReply = _reflection.GeneratedProtocolMessageType('SRv6ManagerReply', (_message.Message,), {
  'DESCRIPTOR' : _SRV6MANAGERREPLY,
  '__module__' : 'srv6_manager_pb2'
  # @@protoc_insertion_point(class_scope:srv6_manager.SRv6ManagerReply)
  })
_sym_db.RegisterMessage(SRv6ManagerReply)

SRv6PathRequest = _reflection.GeneratedProtocolMessageType('SRv6PathRequest', (_message.Message,), {
  'DESCRIPTOR' : _SRV6PATHREQUEST,
  '__module__' : 'srv6_manager_pb2'
  # @@protoc_insertion_point(class_scope:srv6_manager.SRv6PathRequest)
  })
_sym_db.RegisterMessage(SRv6PathRequest)

SRv6PolicyRequest = _reflection.GeneratedProtocolMessageType('SRv6PolicyRequest', (_message.Message,), {
  'DESCRIPTOR' : _SRV6POLICYREQUEST,
  '__module__' : 'srv6_manager_pb2'
  # @@protoc_insertion_point(class_scope:srv6_manager.SRv6PolicyRequest)
  })
_sym_db.RegisterMessage(SRv6PolicyRequest)

SRv6Path = _reflection.GeneratedProtocolMessageType('SRv6Path', (_message.Message,), {

  'SRv6Segment' : _reflection.GeneratedProtocolMessageType('SRv6Segment', (_message.Message,), {
    'DESCRIPTOR' : _SRV6PATH_SRV6SEGMENT,
    '__module__' : 'srv6_manager_pb2'
    # @@protoc_insertion_point(class_scope:srv6_manager.SRv6Path.SRv6Segment)
    })
  ,
  'DESCRIPTOR' : _SRV6PATH,
  '__module__' : 'srv6_manager_pb2'
  # @@protoc_insertion_point(class_scope:srv6_manager.SRv6Path)
  })
_sym_db.RegisterMessage(SRv6Path)
_sym_db.RegisterMessage(SRv6Path.SRv6Segment)

SRv6Policy = _reflection.GeneratedProtocolMessageType('SRv6Policy', (_message.Message,), {

  'SRv6Segment' : _reflection.GeneratedProtocolMessageType('SRv6Segment', (_message.Message,), {
    'DESCRIPTOR' : _SRV6POLICY_SRV6SEGMENT,
    '__module__' : 'srv6_manager_pb2'
    # @@protoc_insertion_point(class_scope:srv6_manager.SRv6Policy.SRv6Segment)
    })
  ,
  'DESCRIPTOR' : _SRV6POLICY,
  '__module__' : 'srv6_manager_pb2'
  # @@protoc_insertion_point(class_scope:srv6_manager.SRv6Policy)
  })
_sym_db.RegisterMessage(SRv6Policy)
_sym_db.RegisterMessage(SRv6Policy.SRv6Segment)

SRv6BehaviorRequest = _reflection.GeneratedProtocolMessageType('SRv6BehaviorRequest', (_message.Message,), {
  'DESCRIPTOR' : _SRV6BEHAVIORREQUEST,
  '__module__' : 'srv6_manager_pb2'
  # @@protoc_insertion_point(class_scope:srv6_manager.SRv6BehaviorRequest)
  })
_sym_db.RegisterMessage(SRv6BehaviorRequest)

SRv6Behavior = _reflection.GeneratedProtocolMessageType('SRv6Behavior', (_message.Message,), {

  'SRv6Segment' : _reflection.GeneratedProtocolMessageType('SRv6Segment', (_message.Message,), {
    'DESCRIPTOR' : _SRV6BEHAVIOR_SRV6SEGMENT,
    '__module__' : 'srv6_manager_pb2'
    # @@protoc_insertion_point(class_scope:srv6_manager.SRv6Behavior.SRv6Segment)
    })
  ,
  'DESCRIPTOR' : _SRV6BEHAVIOR,
  '__module__' : 'srv6_manager_pb2'
  # @@protoc_insertion_point(class_scope:srv6_manager.SRv6Behavior)
  })
_sym_db.RegisterMessage(SRv6Behavior)
_sym_db.RegisterMessage(SRv6Behavior.SRv6Segment)



_SRV6MANAGER = _descriptor.ServiceDescriptor(
  name='SRv6Manager',
  full_name='srv6_manager.SRv6Manager',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=1421,
  serialized_end=1743,
  methods=[
  _descriptor.MethodDescriptor(
    name='Create',
    full_name='srv6_manager.SRv6Manager.Create',
    index=0,
    containing_service=None,
    input_type=_SRV6MANAGERREQUEST,
    output_type=_SRV6MANAGERREPLY,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='Get',
    full_name='srv6_manager.SRv6Manager.Get',
    index=1,
    containing_service=None,
    input_type=_SRV6MANAGERREQUEST,
    output_type=_SRV6MANAGERREPLY,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='Update',
    full_name='srv6_manager.SRv6Manager.Update',
    index=2,
    containing_service=None,
    input_type=_SRV6MANAGERREQUEST,
    output_type=_SRV6MANAGERREPLY,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='Remove',
    full_name='srv6_manager.SRv6Manager.Remove',
    index=3,
    containing_service=None,
    input_type=_SRV6MANAGERREQUEST,
    output_type=_SRV6MANAGERREPLY,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_SRV6MANAGER)

DESCRIPTOR.services_by_name['SRv6Manager'] = _SRV6MANAGER

# @@protoc_insertion_point(module_scope)
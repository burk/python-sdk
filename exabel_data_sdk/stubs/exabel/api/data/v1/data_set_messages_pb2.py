"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....protoc_gen_openapiv2.options import annotations_pb2 as protoc__gen__openapiv2_dot_options_dot_annotations__pb2
DESCRIPTOR = _descriptor.FileDescriptor(name='exabel/api/data/v1/data_set_messages.proto', package='exabel.api.data.v1', syntax='proto3', serialized_options=b'\n\x16com.exabel.api.data.v1B\x14DataSetMessagesProtoP\x01Z\x16exabel.com/api/data/v1', create_key=_descriptor._internal_create_key, serialized_pb=b'\n*exabel/api/data/v1/data_set_messages.proto\x12\x12exabel.api.data.v1\x1a\x1fgoogle/api/field_behavior.proto\x1a.protoc_gen_openapiv2/options/annotations.proto"\xa0\x02\n\x07DataSet\x12>\n\x04name\x18\x01 \x01(\tB0\xe0A\x05\xe0A\x02\x92A\'J\x14"dataSets/ns.stores"\xca>\x0e\xfa\x02\x0bdataSetName\x12#\n\x0cdisplay_name\x18\x02 \x01(\tB\r\x92A\nJ\x08"Stores"\x12>\n\x0bdescription\x18\x03 \x01(\tB)\x92A&J$"The data set of all store entities"\x12N\n\x07signals\x18\x04 \x03(\tB=\xe0A\x06\x92A7J5["signals/ns.customer_amount", "signals/ns.visitors"]\x12 \n\tread_only\x18\x05 \x01(\x08B\r\xe0A\x03\x92A\x07J\x05falseBH\n\x16com.exabel.api.data.v1B\x14DataSetMessagesProtoP\x01Z\x16exabel.com/api/data/v1b\x06proto3', dependencies=[google_dot_api_dot_field__behavior__pb2.DESCRIPTOR, protoc__gen__openapiv2_dot_options_dot_annotations__pb2.DESCRIPTOR])
_DATASET = _descriptor.Descriptor(name='DataSet', full_name='exabel.api.data.v1.DataSet', filename=None, file=DESCRIPTOR, containing_type=None, create_key=_descriptor._internal_create_key, fields=[_descriptor.FieldDescriptor(name='name', full_name='exabel.api.data.v1.DataSet.name', index=0, number=1, type=9, cpp_type=9, label=1, has_default_value=False, default_value=b''.decode('utf-8'), message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, serialized_options=b'\xe0A\x05\xe0A\x02\x92A\'J\x14"dataSets/ns.stores"\xca>\x0e\xfa\x02\x0bdataSetName', file=DESCRIPTOR, create_key=_descriptor._internal_create_key), _descriptor.FieldDescriptor(name='display_name', full_name='exabel.api.data.v1.DataSet.display_name', index=1, number=2, type=9, cpp_type=9, label=1, has_default_value=False, default_value=b''.decode('utf-8'), message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, serialized_options=b'\x92A\nJ\x08"Stores"', file=DESCRIPTOR, create_key=_descriptor._internal_create_key), _descriptor.FieldDescriptor(name='description', full_name='exabel.api.data.v1.DataSet.description', index=2, number=3, type=9, cpp_type=9, label=1, has_default_value=False, default_value=b''.decode('utf-8'), message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, serialized_options=b'\x92A&J$"The data set of all store entities"', file=DESCRIPTOR, create_key=_descriptor._internal_create_key), _descriptor.FieldDescriptor(name='signals', full_name='exabel.api.data.v1.DataSet.signals', index=3, number=4, type=9, cpp_type=9, label=3, has_default_value=False, default_value=[], message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, serialized_options=b'\xe0A\x06\x92A7J5["signals/ns.customer_amount", "signals/ns.visitors"]', file=DESCRIPTOR, create_key=_descriptor._internal_create_key), _descriptor.FieldDescriptor(name='read_only', full_name='exabel.api.data.v1.DataSet.read_only', index=4, number=5, type=8, cpp_type=7, label=1, has_default_value=False, default_value=False, message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, serialized_options=b'\xe0A\x03\x92A\x07J\x05false', file=DESCRIPTOR, create_key=_descriptor._internal_create_key)], extensions=[], nested_types=[], enum_types=[], serialized_options=None, is_extendable=False, syntax='proto3', extension_ranges=[], oneofs=[], serialized_start=148, serialized_end=436)
DESCRIPTOR.message_types_by_name['DataSet'] = _DATASET
_sym_db.RegisterFileDescriptor(DESCRIPTOR)
DataSet = _reflection.GeneratedProtocolMessageType('DataSet', (_message.Message,), {'DESCRIPTOR': _DATASET, '__module__': 'exabel.api.data.v1.data_set_messages_pb2'})
_sym_db.RegisterMessage(DataSet)
DESCRIPTOR._options = None
_DATASET.fields_by_name['name']._options = None
_DATASET.fields_by_name['display_name']._options = None
_DATASET.fields_by_name['description']._options = None
_DATASET.fields_by_name['signals']._options = None
_DATASET.fields_by_name['read_only']._options = None
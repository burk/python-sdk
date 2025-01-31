"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from google.protobuf import descriptor_pb2 as google_dot_protobuf_dot_descriptor__pb2
from ...protoc_gen_openapiv2.options import openapiv2_pb2 as protoc__gen__openapiv2_dot_options_dot_openapiv2__pb2
DESCRIPTOR = _descriptor.FileDescriptor(name='protoc_gen_openapiv2/options/annotations.proto', package='grpc.gateway.protoc_gen_openapiv2.options', syntax='proto3', serialized_options=b'ZFgithub.com/grpc-ecosystem/grpc-gateway/v2/protoc-gen-openapiv2/options', create_key=_descriptor._internal_create_key, serialized_pb=b'\n.protoc_gen_openapiv2/options/annotations.proto\x12)grpc.gateway.protoc_gen_openapiv2.options\x1a google/protobuf/descriptor.proto\x1a,protoc_gen_openapiv2/options/openapiv2.proto:l\n\x11openapiv2_swagger\x12\x1c.google.protobuf.FileOptions\x18\x92\x08 \x01(\x0b22.grpc.gateway.protoc_gen_openapiv2.options.Swagger:r\n\x13openapiv2_operation\x12\x1e.google.protobuf.MethodOptions\x18\x92\x08 \x01(\x0b24.grpc.gateway.protoc_gen_openapiv2.options.Operation:m\n\x10openapiv2_schema\x12\x1f.google.protobuf.MessageOptions\x18\x92\x08 \x01(\x0b21.grpc.gateway.protoc_gen_openapiv2.options.Schema:g\n\ropenapiv2_tag\x12\x1f.google.protobuf.ServiceOptions\x18\x92\x08 \x01(\x0b2..grpc.gateway.protoc_gen_openapiv2.options.Tag:n\n\x0fopenapiv2_field\x12\x1d.google.protobuf.FieldOptions\x18\x92\x08 \x01(\x0b25.grpc.gateway.protoc_gen_openapiv2.options.JSONSchemaBHZFgithub.com/grpc-ecosystem/grpc-gateway/v2/protoc-gen-openapiv2/optionsb\x06proto3', dependencies=[google_dot_protobuf_dot_descriptor__pb2.DESCRIPTOR, protoc__gen__openapiv2_dot_options_dot_openapiv2__pb2.DESCRIPTOR])
OPENAPIV2_SWAGGER_FIELD_NUMBER = 1042
openapiv2_swagger = _descriptor.FieldDescriptor(name='openapiv2_swagger', full_name='grpc.gateway.protoc_gen_openapiv2.options.openapiv2_swagger', index=0, number=1042, type=11, cpp_type=10, label=1, has_default_value=False, default_value=None, message_type=None, enum_type=None, containing_type=None, is_extension=True, extension_scope=None, serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key)
OPENAPIV2_OPERATION_FIELD_NUMBER = 1042
openapiv2_operation = _descriptor.FieldDescriptor(name='openapiv2_operation', full_name='grpc.gateway.protoc_gen_openapiv2.options.openapiv2_operation', index=1, number=1042, type=11, cpp_type=10, label=1, has_default_value=False, default_value=None, message_type=None, enum_type=None, containing_type=None, is_extension=True, extension_scope=None, serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key)
OPENAPIV2_SCHEMA_FIELD_NUMBER = 1042
openapiv2_schema = _descriptor.FieldDescriptor(name='openapiv2_schema', full_name='grpc.gateway.protoc_gen_openapiv2.options.openapiv2_schema', index=2, number=1042, type=11, cpp_type=10, label=1, has_default_value=False, default_value=None, message_type=None, enum_type=None, containing_type=None, is_extension=True, extension_scope=None, serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key)
OPENAPIV2_TAG_FIELD_NUMBER = 1042
openapiv2_tag = _descriptor.FieldDescriptor(name='openapiv2_tag', full_name='grpc.gateway.protoc_gen_openapiv2.options.openapiv2_tag', index=3, number=1042, type=11, cpp_type=10, label=1, has_default_value=False, default_value=None, message_type=None, enum_type=None, containing_type=None, is_extension=True, extension_scope=None, serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key)
OPENAPIV2_FIELD_FIELD_NUMBER = 1042
openapiv2_field = _descriptor.FieldDescriptor(name='openapiv2_field', full_name='grpc.gateway.protoc_gen_openapiv2.options.openapiv2_field', index=4, number=1042, type=11, cpp_type=10, label=1, has_default_value=False, default_value=None, message_type=None, enum_type=None, containing_type=None, is_extension=True, extension_scope=None, serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key)
DESCRIPTOR.extensions_by_name['openapiv2_swagger'] = openapiv2_swagger
DESCRIPTOR.extensions_by_name['openapiv2_operation'] = openapiv2_operation
DESCRIPTOR.extensions_by_name['openapiv2_schema'] = openapiv2_schema
DESCRIPTOR.extensions_by_name['openapiv2_tag'] = openapiv2_tag
DESCRIPTOR.extensions_by_name['openapiv2_field'] = openapiv2_field
_sym_db.RegisterFileDescriptor(DESCRIPTOR)
openapiv2_swagger.message_type = protoc__gen__openapiv2_dot_options_dot_openapiv2__pb2._SWAGGER
google_dot_protobuf_dot_descriptor__pb2.FileOptions.RegisterExtension(openapiv2_swagger)
openapiv2_operation.message_type = protoc__gen__openapiv2_dot_options_dot_openapiv2__pb2._OPERATION
google_dot_protobuf_dot_descriptor__pb2.MethodOptions.RegisterExtension(openapiv2_operation)
openapiv2_schema.message_type = protoc__gen__openapiv2_dot_options_dot_openapiv2__pb2._SCHEMA
google_dot_protobuf_dot_descriptor__pb2.MessageOptions.RegisterExtension(openapiv2_schema)
openapiv2_tag.message_type = protoc__gen__openapiv2_dot_options_dot_openapiv2__pb2._TAG
google_dot_protobuf_dot_descriptor__pb2.ServiceOptions.RegisterExtension(openapiv2_tag)
openapiv2_field.message_type = protoc__gen__openapiv2_dot_options_dot_openapiv2__pb2._JSONSCHEMA
google_dot_protobuf_dot_descriptor__pb2.FieldOptions.RegisterExtension(openapiv2_field)
DESCRIPTOR._options = None
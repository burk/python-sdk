"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
from google.protobuf.descriptor import Descriptor as google___protobuf___descriptor___Descriptor, EnumDescriptor as google___protobuf___descriptor___EnumDescriptor, FileDescriptor as google___protobuf___descriptor___FileDescriptor
from google.protobuf.internal.containers import MessageMap as google___protobuf___internal___containers___MessageMap, RepeatedCompositeFieldContainer as google___protobuf___internal___containers___RepeatedCompositeFieldContainer, RepeatedScalarFieldContainer as google___protobuf___internal___containers___RepeatedScalarFieldContainer, ScalarMap as google___protobuf___internal___containers___ScalarMap
from google.protobuf.internal.enum_type_wrapper import _EnumTypeWrapper as google___protobuf___internal___enum_type_wrapper____EnumTypeWrapper
from google.protobuf.message import Message as google___protobuf___message___Message
from google.protobuf.struct_pb2 import Value as google___protobuf___struct_pb2___Value
from typing import Iterable as typing___Iterable, Mapping as typing___Mapping, NewType as typing___NewType, Optional as typing___Optional, Text as typing___Text, cast as typing___cast
from typing_extensions import Literal as typing_extensions___Literal
builtin___bool = bool
builtin___bytes = bytes
builtin___float = float
builtin___int = int
DESCRIPTOR: google___protobuf___descriptor___FileDescriptor = ...
SchemeValue = typing___NewType('SchemeValue', builtin___int)
type___SchemeValue = SchemeValue
Scheme: _Scheme

class _Scheme(google___protobuf___internal___enum_type_wrapper____EnumTypeWrapper[SchemeValue]):
    DESCRIPTOR: google___protobuf___descriptor___EnumDescriptor = ...
    UNKNOWN = typing___cast(SchemeValue, 0)
    HTTP = typing___cast(SchemeValue, 1)
    HTTPS = typing___cast(SchemeValue, 2)
    WS = typing___cast(SchemeValue, 3)
    WSS = typing___cast(SchemeValue, 4)
UNKNOWN = typing___cast(SchemeValue, 0)
HTTP = typing___cast(SchemeValue, 1)
HTTPS = typing___cast(SchemeValue, 2)
WS = typing___cast(SchemeValue, 3)
WSS = typing___cast(SchemeValue, 4)

class Swagger(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...

    class ResponsesEntry(google___protobuf___message___Message):
        DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
        key: typing___Text = ...

        @property
        def value(self) -> type___Response:
            ...

        def __init__(self, *, key: typing___Optional[typing___Text]=None, value: typing___Optional[type___Response]=None) -> None:
            ...

        def HasField(self, field_name: typing_extensions___Literal[u'value', b'value']) -> builtin___bool:
            ...

        def ClearField(self, field_name: typing_extensions___Literal[u'key', b'key', u'value', b'value']) -> None:
            ...
    type___ResponsesEntry = ResponsesEntry

    class ExtensionsEntry(google___protobuf___message___Message):
        DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
        key: typing___Text = ...

        @property
        def value(self) -> google___protobuf___struct_pb2___Value:
            ...

        def __init__(self, *, key: typing___Optional[typing___Text]=None, value: typing___Optional[google___protobuf___struct_pb2___Value]=None) -> None:
            ...

        def HasField(self, field_name: typing_extensions___Literal[u'value', b'value']) -> builtin___bool:
            ...

        def ClearField(self, field_name: typing_extensions___Literal[u'key', b'key', u'value', b'value']) -> None:
            ...
    type___ExtensionsEntry = ExtensionsEntry
    swagger: typing___Text = ...
    host: typing___Text = ...
    base_path: typing___Text = ...
    schemes: google___protobuf___internal___containers___RepeatedScalarFieldContainer[type___SchemeValue] = ...
    consumes: google___protobuf___internal___containers___RepeatedScalarFieldContainer[typing___Text] = ...
    produces: google___protobuf___internal___containers___RepeatedScalarFieldContainer[typing___Text] = ...

    @property
    def info(self) -> type___Info:
        ...

    @property
    def responses(self) -> google___protobuf___internal___containers___MessageMap[typing___Text, type___Response]:
        ...

    @property
    def security_definitions(self) -> type___SecurityDefinitions:
        ...

    @property
    def security(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[type___SecurityRequirement]:
        ...

    @property
    def external_docs(self) -> type___ExternalDocumentation:
        ...

    @property
    def extensions(self) -> google___protobuf___internal___containers___MessageMap[typing___Text, google___protobuf___struct_pb2___Value]:
        ...

    def __init__(self, *, swagger: typing___Optional[typing___Text]=None, info: typing___Optional[type___Info]=None, host: typing___Optional[typing___Text]=None, base_path: typing___Optional[typing___Text]=None, schemes: typing___Optional[typing___Iterable[type___SchemeValue]]=None, consumes: typing___Optional[typing___Iterable[typing___Text]]=None, produces: typing___Optional[typing___Iterable[typing___Text]]=None, responses: typing___Optional[typing___Mapping[typing___Text, type___Response]]=None, security_definitions: typing___Optional[type___SecurityDefinitions]=None, security: typing___Optional[typing___Iterable[type___SecurityRequirement]]=None, external_docs: typing___Optional[type___ExternalDocumentation]=None, extensions: typing___Optional[typing___Mapping[typing___Text, google___protobuf___struct_pb2___Value]]=None) -> None:
        ...

    def HasField(self, field_name: typing_extensions___Literal[u'external_docs', b'external_docs', u'info', b'info', u'security_definitions', b'security_definitions']) -> builtin___bool:
        ...

    def ClearField(self, field_name: typing_extensions___Literal[u'base_path', b'base_path', u'consumes', b'consumes', u'extensions', b'extensions', u'external_docs', b'external_docs', u'host', b'host', u'info', b'info', u'produces', b'produces', u'responses', b'responses', u'schemes', b'schemes', u'security', b'security', u'security_definitions', b'security_definitions', u'swagger', b'swagger']) -> None:
        ...
type___Swagger = Swagger

class Operation(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...

    class ResponsesEntry(google___protobuf___message___Message):
        DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
        key: typing___Text = ...

        @property
        def value(self) -> type___Response:
            ...

        def __init__(self, *, key: typing___Optional[typing___Text]=None, value: typing___Optional[type___Response]=None) -> None:
            ...

        def HasField(self, field_name: typing_extensions___Literal[u'value', b'value']) -> builtin___bool:
            ...

        def ClearField(self, field_name: typing_extensions___Literal[u'key', b'key', u'value', b'value']) -> None:
            ...
    type___ResponsesEntry = ResponsesEntry

    class ExtensionsEntry(google___protobuf___message___Message):
        DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
        key: typing___Text = ...

        @property
        def value(self) -> google___protobuf___struct_pb2___Value:
            ...

        def __init__(self, *, key: typing___Optional[typing___Text]=None, value: typing___Optional[google___protobuf___struct_pb2___Value]=None) -> None:
            ...

        def HasField(self, field_name: typing_extensions___Literal[u'value', b'value']) -> builtin___bool:
            ...

        def ClearField(self, field_name: typing_extensions___Literal[u'key', b'key', u'value', b'value']) -> None:
            ...
    type___ExtensionsEntry = ExtensionsEntry
    tags: google___protobuf___internal___containers___RepeatedScalarFieldContainer[typing___Text] = ...
    summary: typing___Text = ...
    description: typing___Text = ...
    operation_id: typing___Text = ...
    consumes: google___protobuf___internal___containers___RepeatedScalarFieldContainer[typing___Text] = ...
    produces: google___protobuf___internal___containers___RepeatedScalarFieldContainer[typing___Text] = ...
    schemes: google___protobuf___internal___containers___RepeatedScalarFieldContainer[type___SchemeValue] = ...
    deprecated: builtin___bool = ...

    @property
    def external_docs(self) -> type___ExternalDocumentation:
        ...

    @property
    def responses(self) -> google___protobuf___internal___containers___MessageMap[typing___Text, type___Response]:
        ...

    @property
    def security(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[type___SecurityRequirement]:
        ...

    @property
    def extensions(self) -> google___protobuf___internal___containers___MessageMap[typing___Text, google___protobuf___struct_pb2___Value]:
        ...

    def __init__(self, *, tags: typing___Optional[typing___Iterable[typing___Text]]=None, summary: typing___Optional[typing___Text]=None, description: typing___Optional[typing___Text]=None, external_docs: typing___Optional[type___ExternalDocumentation]=None, operation_id: typing___Optional[typing___Text]=None, consumes: typing___Optional[typing___Iterable[typing___Text]]=None, produces: typing___Optional[typing___Iterable[typing___Text]]=None, responses: typing___Optional[typing___Mapping[typing___Text, type___Response]]=None, schemes: typing___Optional[typing___Iterable[type___SchemeValue]]=None, deprecated: typing___Optional[builtin___bool]=None, security: typing___Optional[typing___Iterable[type___SecurityRequirement]]=None, extensions: typing___Optional[typing___Mapping[typing___Text, google___protobuf___struct_pb2___Value]]=None) -> None:
        ...

    def HasField(self, field_name: typing_extensions___Literal[u'external_docs', b'external_docs']) -> builtin___bool:
        ...

    def ClearField(self, field_name: typing_extensions___Literal[u'consumes', b'consumes', u'deprecated', b'deprecated', u'description', b'description', u'extensions', b'extensions', u'external_docs', b'external_docs', u'operation_id', b'operation_id', u'produces', b'produces', u'responses', b'responses', u'schemes', b'schemes', u'security', b'security', u'summary', b'summary', u'tags', b'tags']) -> None:
        ...
type___Operation = Operation

class Header(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    description: typing___Text = ...
    type: typing___Text = ...
    format: typing___Text = ...
    default: typing___Text = ...
    pattern: typing___Text = ...

    def __init__(self, *, description: typing___Optional[typing___Text]=None, type: typing___Optional[typing___Text]=None, format: typing___Optional[typing___Text]=None, default: typing___Optional[typing___Text]=None, pattern: typing___Optional[typing___Text]=None) -> None:
        ...

    def ClearField(self, field_name: typing_extensions___Literal[u'default', b'default', u'description', b'description', u'format', b'format', u'pattern', b'pattern', u'type', b'type']) -> None:
        ...
type___Header = Header

class Response(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...

    class HeadersEntry(google___protobuf___message___Message):
        DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
        key: typing___Text = ...

        @property
        def value(self) -> type___Header:
            ...

        def __init__(self, *, key: typing___Optional[typing___Text]=None, value: typing___Optional[type___Header]=None) -> None:
            ...

        def HasField(self, field_name: typing_extensions___Literal[u'value', b'value']) -> builtin___bool:
            ...

        def ClearField(self, field_name: typing_extensions___Literal[u'key', b'key', u'value', b'value']) -> None:
            ...
    type___HeadersEntry = HeadersEntry

    class ExamplesEntry(google___protobuf___message___Message):
        DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
        key: typing___Text = ...
        value: typing___Text = ...

        def __init__(self, *, key: typing___Optional[typing___Text]=None, value: typing___Optional[typing___Text]=None) -> None:
            ...

        def ClearField(self, field_name: typing_extensions___Literal[u'key', b'key', u'value', b'value']) -> None:
            ...
    type___ExamplesEntry = ExamplesEntry

    class ExtensionsEntry(google___protobuf___message___Message):
        DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
        key: typing___Text = ...

        @property
        def value(self) -> google___protobuf___struct_pb2___Value:
            ...

        def __init__(self, *, key: typing___Optional[typing___Text]=None, value: typing___Optional[google___protobuf___struct_pb2___Value]=None) -> None:
            ...

        def HasField(self, field_name: typing_extensions___Literal[u'value', b'value']) -> builtin___bool:
            ...

        def ClearField(self, field_name: typing_extensions___Literal[u'key', b'key', u'value', b'value']) -> None:
            ...
    type___ExtensionsEntry = ExtensionsEntry
    description: typing___Text = ...

    @property
    def schema(self) -> type___Schema:
        ...

    @property
    def headers(self) -> google___protobuf___internal___containers___MessageMap[typing___Text, type___Header]:
        ...

    @property
    def examples(self) -> google___protobuf___internal___containers___ScalarMap[typing___Text, typing___Text]:
        ...

    @property
    def extensions(self) -> google___protobuf___internal___containers___MessageMap[typing___Text, google___protobuf___struct_pb2___Value]:
        ...

    def __init__(self, *, description: typing___Optional[typing___Text]=None, schema: typing___Optional[type___Schema]=None, headers: typing___Optional[typing___Mapping[typing___Text, type___Header]]=None, examples: typing___Optional[typing___Mapping[typing___Text, typing___Text]]=None, extensions: typing___Optional[typing___Mapping[typing___Text, google___protobuf___struct_pb2___Value]]=None) -> None:
        ...

    def HasField(self, field_name: typing_extensions___Literal[u'schema', b'schema']) -> builtin___bool:
        ...

    def ClearField(self, field_name: typing_extensions___Literal[u'description', b'description', u'examples', b'examples', u'extensions', b'extensions', u'headers', b'headers', u'schema', b'schema']) -> None:
        ...
type___Response = Response

class Info(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...

    class ExtensionsEntry(google___protobuf___message___Message):
        DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
        key: typing___Text = ...

        @property
        def value(self) -> google___protobuf___struct_pb2___Value:
            ...

        def __init__(self, *, key: typing___Optional[typing___Text]=None, value: typing___Optional[google___protobuf___struct_pb2___Value]=None) -> None:
            ...

        def HasField(self, field_name: typing_extensions___Literal[u'value', b'value']) -> builtin___bool:
            ...

        def ClearField(self, field_name: typing_extensions___Literal[u'key', b'key', u'value', b'value']) -> None:
            ...
    type___ExtensionsEntry = ExtensionsEntry
    title: typing___Text = ...
    description: typing___Text = ...
    terms_of_service: typing___Text = ...
    version: typing___Text = ...

    @property
    def contact(self) -> type___Contact:
        ...

    @property
    def license(self) -> type___License:
        ...

    @property
    def extensions(self) -> google___protobuf___internal___containers___MessageMap[typing___Text, google___protobuf___struct_pb2___Value]:
        ...

    def __init__(self, *, title: typing___Optional[typing___Text]=None, description: typing___Optional[typing___Text]=None, terms_of_service: typing___Optional[typing___Text]=None, contact: typing___Optional[type___Contact]=None, license: typing___Optional[type___License]=None, version: typing___Optional[typing___Text]=None, extensions: typing___Optional[typing___Mapping[typing___Text, google___protobuf___struct_pb2___Value]]=None) -> None:
        ...

    def HasField(self, field_name: typing_extensions___Literal[u'contact', b'contact', u'license', b'license']) -> builtin___bool:
        ...

    def ClearField(self, field_name: typing_extensions___Literal[u'contact', b'contact', u'description', b'description', u'extensions', b'extensions', u'license', b'license', u'terms_of_service', b'terms_of_service', u'title', b'title', u'version', b'version']) -> None:
        ...
type___Info = Info

class Contact(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    name: typing___Text = ...
    url: typing___Text = ...
    email: typing___Text = ...

    def __init__(self, *, name: typing___Optional[typing___Text]=None, url: typing___Optional[typing___Text]=None, email: typing___Optional[typing___Text]=None) -> None:
        ...

    def ClearField(self, field_name: typing_extensions___Literal[u'email', b'email', u'name', b'name', u'url', b'url']) -> None:
        ...
type___Contact = Contact

class License(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    name: typing___Text = ...
    url: typing___Text = ...

    def __init__(self, *, name: typing___Optional[typing___Text]=None, url: typing___Optional[typing___Text]=None) -> None:
        ...

    def ClearField(self, field_name: typing_extensions___Literal[u'name', b'name', u'url', b'url']) -> None:
        ...
type___License = License

class ExternalDocumentation(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    description: typing___Text = ...
    url: typing___Text = ...

    def __init__(self, *, description: typing___Optional[typing___Text]=None, url: typing___Optional[typing___Text]=None) -> None:
        ...

    def ClearField(self, field_name: typing_extensions___Literal[u'description', b'description', u'url', b'url']) -> None:
        ...
type___ExternalDocumentation = ExternalDocumentation

class Schema(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    discriminator: typing___Text = ...
    read_only: builtin___bool = ...
    example: typing___Text = ...

    @property
    def json_schema(self) -> type___JSONSchema:
        ...

    @property
    def external_docs(self) -> type___ExternalDocumentation:
        ...

    def __init__(self, *, json_schema: typing___Optional[type___JSONSchema]=None, discriminator: typing___Optional[typing___Text]=None, read_only: typing___Optional[builtin___bool]=None, external_docs: typing___Optional[type___ExternalDocumentation]=None, example: typing___Optional[typing___Text]=None) -> None:
        ...

    def HasField(self, field_name: typing_extensions___Literal[u'external_docs', b'external_docs', u'json_schema', b'json_schema']) -> builtin___bool:
        ...

    def ClearField(self, field_name: typing_extensions___Literal[u'discriminator', b'discriminator', u'example', b'example', u'external_docs', b'external_docs', u'json_schema', b'json_schema', u'read_only', b'read_only']) -> None:
        ...
type___Schema = Schema

class JSONSchema(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    JSONSchemaSimpleTypesValue = typing___NewType('JSONSchemaSimpleTypesValue', builtin___int)
    type___JSONSchemaSimpleTypesValue = JSONSchemaSimpleTypesValue
    JSONSchemaSimpleTypes: _JSONSchemaSimpleTypes

    class _JSONSchemaSimpleTypes(google___protobuf___internal___enum_type_wrapper____EnumTypeWrapper[JSONSchema.JSONSchemaSimpleTypesValue]):
        DESCRIPTOR: google___protobuf___descriptor___EnumDescriptor = ...
        UNKNOWN = typing___cast(JSONSchema.JSONSchemaSimpleTypesValue, 0)
        ARRAY = typing___cast(JSONSchema.JSONSchemaSimpleTypesValue, 1)
        BOOLEAN = typing___cast(JSONSchema.JSONSchemaSimpleTypesValue, 2)
        INTEGER = typing___cast(JSONSchema.JSONSchemaSimpleTypesValue, 3)
        NULL = typing___cast(JSONSchema.JSONSchemaSimpleTypesValue, 4)
        NUMBER = typing___cast(JSONSchema.JSONSchemaSimpleTypesValue, 5)
        OBJECT = typing___cast(JSONSchema.JSONSchemaSimpleTypesValue, 6)
        STRING = typing___cast(JSONSchema.JSONSchemaSimpleTypesValue, 7)
    UNKNOWN = typing___cast(JSONSchema.JSONSchemaSimpleTypesValue, 0)
    ARRAY = typing___cast(JSONSchema.JSONSchemaSimpleTypesValue, 1)
    BOOLEAN = typing___cast(JSONSchema.JSONSchemaSimpleTypesValue, 2)
    INTEGER = typing___cast(JSONSchema.JSONSchemaSimpleTypesValue, 3)
    NULL = typing___cast(JSONSchema.JSONSchemaSimpleTypesValue, 4)
    NUMBER = typing___cast(JSONSchema.JSONSchemaSimpleTypesValue, 5)
    OBJECT = typing___cast(JSONSchema.JSONSchemaSimpleTypesValue, 6)
    STRING = typing___cast(JSONSchema.JSONSchemaSimpleTypesValue, 7)
    ref: typing___Text = ...
    title: typing___Text = ...
    description: typing___Text = ...
    default: typing___Text = ...
    read_only: builtin___bool = ...
    example: typing___Text = ...
    multiple_of: builtin___float = ...
    maximum: builtin___float = ...
    exclusive_maximum: builtin___bool = ...
    minimum: builtin___float = ...
    exclusive_minimum: builtin___bool = ...
    max_length: builtin___int = ...
    min_length: builtin___int = ...
    pattern: typing___Text = ...
    max_items: builtin___int = ...
    min_items: builtin___int = ...
    unique_items: builtin___bool = ...
    max_properties: builtin___int = ...
    min_properties: builtin___int = ...
    required: google___protobuf___internal___containers___RepeatedScalarFieldContainer[typing___Text] = ...
    array: google___protobuf___internal___containers___RepeatedScalarFieldContainer[typing___Text] = ...
    type: google___protobuf___internal___containers___RepeatedScalarFieldContainer[type___JSONSchema.JSONSchemaSimpleTypesValue] = ...
    format: typing___Text = ...
    enum: google___protobuf___internal___containers___RepeatedScalarFieldContainer[typing___Text] = ...
    path_param_name: typing___Text = ...

    def __init__(self, *, ref: typing___Optional[typing___Text]=None, title: typing___Optional[typing___Text]=None, description: typing___Optional[typing___Text]=None, default: typing___Optional[typing___Text]=None, read_only: typing___Optional[builtin___bool]=None, example: typing___Optional[typing___Text]=None, multiple_of: typing___Optional[builtin___float]=None, maximum: typing___Optional[builtin___float]=None, exclusive_maximum: typing___Optional[builtin___bool]=None, minimum: typing___Optional[builtin___float]=None, exclusive_minimum: typing___Optional[builtin___bool]=None, max_length: typing___Optional[builtin___int]=None, min_length: typing___Optional[builtin___int]=None, pattern: typing___Optional[typing___Text]=None, max_items: typing___Optional[builtin___int]=None, min_items: typing___Optional[builtin___int]=None, unique_items: typing___Optional[builtin___bool]=None, max_properties: typing___Optional[builtin___int]=None, min_properties: typing___Optional[builtin___int]=None, required: typing___Optional[typing___Iterable[typing___Text]]=None, array: typing___Optional[typing___Iterable[typing___Text]]=None, type: typing___Optional[typing___Iterable[type___JSONSchema.JSONSchemaSimpleTypesValue]]=None, format: typing___Optional[typing___Text]=None, enum: typing___Optional[typing___Iterable[typing___Text]]=None, path_param_name: typing___Optional[typing___Text]=None) -> None:
        ...

    def ClearField(self, field_name: typing_extensions___Literal[u'array', b'array', u'default', b'default', u'description', b'description', u'enum', b'enum', u'example', b'example', u'exclusive_maximum', b'exclusive_maximum', u'exclusive_minimum', b'exclusive_minimum', u'format', b'format', u'max_items', b'max_items', u'max_length', b'max_length', u'max_properties', b'max_properties', u'maximum', b'maximum', u'min_items', b'min_items', u'min_length', b'min_length', u'min_properties', b'min_properties', u'minimum', b'minimum', u'multiple_of', b'multiple_of', u'path_param_name', b'path_param_name', u'pattern', b'pattern', u'read_only', b'read_only', u'ref', b'ref', u'required', b'required', u'title', b'title', u'type', b'type', u'unique_items', b'unique_items']) -> None:
        ...
type___JSONSchema = JSONSchema

class Tag(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    description: typing___Text = ...

    @property
    def external_docs(self) -> type___ExternalDocumentation:
        ...

    def __init__(self, *, description: typing___Optional[typing___Text]=None, external_docs: typing___Optional[type___ExternalDocumentation]=None) -> None:
        ...

    def HasField(self, field_name: typing_extensions___Literal[u'external_docs', b'external_docs']) -> builtin___bool:
        ...

    def ClearField(self, field_name: typing_extensions___Literal[u'description', b'description', u'external_docs', b'external_docs']) -> None:
        ...
type___Tag = Tag

class SecurityDefinitions(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...

    class SecurityEntry(google___protobuf___message___Message):
        DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
        key: typing___Text = ...

        @property
        def value(self) -> type___SecurityScheme:
            ...

        def __init__(self, *, key: typing___Optional[typing___Text]=None, value: typing___Optional[type___SecurityScheme]=None) -> None:
            ...

        def HasField(self, field_name: typing_extensions___Literal[u'value', b'value']) -> builtin___bool:
            ...

        def ClearField(self, field_name: typing_extensions___Literal[u'key', b'key', u'value', b'value']) -> None:
            ...
    type___SecurityEntry = SecurityEntry

    @property
    def security(self) -> google___protobuf___internal___containers___MessageMap[typing___Text, type___SecurityScheme]:
        ...

    def __init__(self, *, security: typing___Optional[typing___Mapping[typing___Text, type___SecurityScheme]]=None) -> None:
        ...

    def ClearField(self, field_name: typing_extensions___Literal[u'security', b'security']) -> None:
        ...
type___SecurityDefinitions = SecurityDefinitions

class SecurityScheme(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    TypeValue = typing___NewType('TypeValue', builtin___int)
    type___TypeValue = TypeValue
    Type: _Type

    class _Type(google___protobuf___internal___enum_type_wrapper____EnumTypeWrapper[SecurityScheme.TypeValue]):
        DESCRIPTOR: google___protobuf___descriptor___EnumDescriptor = ...
        TYPE_INVALID = typing___cast(SecurityScheme.TypeValue, 0)
        TYPE_BASIC = typing___cast(SecurityScheme.TypeValue, 1)
        TYPE_API_KEY = typing___cast(SecurityScheme.TypeValue, 2)
        TYPE_OAUTH2 = typing___cast(SecurityScheme.TypeValue, 3)
    TYPE_INVALID = typing___cast(SecurityScheme.TypeValue, 0)
    TYPE_BASIC = typing___cast(SecurityScheme.TypeValue, 1)
    TYPE_API_KEY = typing___cast(SecurityScheme.TypeValue, 2)
    TYPE_OAUTH2 = typing___cast(SecurityScheme.TypeValue, 3)
    InValue = typing___NewType('InValue', builtin___int)
    type___InValue = InValue
    In: _In

    class _In(google___protobuf___internal___enum_type_wrapper____EnumTypeWrapper[SecurityScheme.InValue]):
        DESCRIPTOR: google___protobuf___descriptor___EnumDescriptor = ...
        IN_INVALID = typing___cast(SecurityScheme.InValue, 0)
        IN_QUERY = typing___cast(SecurityScheme.InValue, 1)
        IN_HEADER = typing___cast(SecurityScheme.InValue, 2)
    IN_INVALID = typing___cast(SecurityScheme.InValue, 0)
    IN_QUERY = typing___cast(SecurityScheme.InValue, 1)
    IN_HEADER = typing___cast(SecurityScheme.InValue, 2)
    FlowValue = typing___NewType('FlowValue', builtin___int)
    type___FlowValue = FlowValue
    Flow: _Flow

    class _Flow(google___protobuf___internal___enum_type_wrapper____EnumTypeWrapper[SecurityScheme.FlowValue]):
        DESCRIPTOR: google___protobuf___descriptor___EnumDescriptor = ...
        FLOW_INVALID = typing___cast(SecurityScheme.FlowValue, 0)
        FLOW_IMPLICIT = typing___cast(SecurityScheme.FlowValue, 1)
        FLOW_PASSWORD = typing___cast(SecurityScheme.FlowValue, 2)
        FLOW_APPLICATION = typing___cast(SecurityScheme.FlowValue, 3)
        FLOW_ACCESS_CODE = typing___cast(SecurityScheme.FlowValue, 4)
    FLOW_INVALID = typing___cast(SecurityScheme.FlowValue, 0)
    FLOW_IMPLICIT = typing___cast(SecurityScheme.FlowValue, 1)
    FLOW_PASSWORD = typing___cast(SecurityScheme.FlowValue, 2)
    FLOW_APPLICATION = typing___cast(SecurityScheme.FlowValue, 3)
    FLOW_ACCESS_CODE = typing___cast(SecurityScheme.FlowValue, 4)

    class ExtensionsEntry(google___protobuf___message___Message):
        DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
        key: typing___Text = ...

        @property
        def value(self) -> google___protobuf___struct_pb2___Value:
            ...

        def __init__(self, *, key: typing___Optional[typing___Text]=None, value: typing___Optional[google___protobuf___struct_pb2___Value]=None) -> None:
            ...

        def HasField(self, field_name: typing_extensions___Literal[u'value', b'value']) -> builtin___bool:
            ...

        def ClearField(self, field_name: typing_extensions___Literal[u'key', b'key', u'value', b'value']) -> None:
            ...
    type___ExtensionsEntry = ExtensionsEntry
    type: type___SecurityScheme.TypeValue = ...
    description: typing___Text = ...
    name: typing___Text = ...
    flow: type___SecurityScheme.FlowValue = ...
    authorization_url: typing___Text = ...
    token_url: typing___Text = ...

    @property
    def scopes(self) -> type___Scopes:
        ...

    @property
    def extensions(self) -> google___protobuf___internal___containers___MessageMap[typing___Text, google___protobuf___struct_pb2___Value]:
        ...

    def __init__(self, *, type: typing___Optional[type___SecurityScheme.TypeValue]=None, description: typing___Optional[typing___Text]=None, name: typing___Optional[typing___Text]=None, flow: typing___Optional[type___SecurityScheme.FlowValue]=None, authorization_url: typing___Optional[typing___Text]=None, token_url: typing___Optional[typing___Text]=None, scopes: typing___Optional[type___Scopes]=None, extensions: typing___Optional[typing___Mapping[typing___Text, google___protobuf___struct_pb2___Value]]=None) -> None:
        ...

    def HasField(self, field_name: typing_extensions___Literal[u'scopes', b'scopes']) -> builtin___bool:
        ...

    def ClearField(self, field_name: typing_extensions___Literal[u'authorization_url', b'authorization_url', u'description', b'description', u'extensions', b'extensions', u'flow', b'flow', u'in', b'in', u'name', b'name', u'scopes', b'scopes', u'token_url', b'token_url', u'type', b'type']) -> None:
        ...
type___SecurityScheme = SecurityScheme

class SecurityRequirement(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...

    class SecurityRequirementValue(google___protobuf___message___Message):
        DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
        scope: google___protobuf___internal___containers___RepeatedScalarFieldContainer[typing___Text] = ...

        def __init__(self, *, scope: typing___Optional[typing___Iterable[typing___Text]]=None) -> None:
            ...

        def ClearField(self, field_name: typing_extensions___Literal[u'scope', b'scope']) -> None:
            ...
    type___SecurityRequirementValue = SecurityRequirementValue

    class SecurityRequirementEntry(google___protobuf___message___Message):
        DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
        key: typing___Text = ...

        @property
        def value(self) -> type___SecurityRequirement.SecurityRequirementValue:
            ...

        def __init__(self, *, key: typing___Optional[typing___Text]=None, value: typing___Optional[type___SecurityRequirement.SecurityRequirementValue]=None) -> None:
            ...

        def HasField(self, field_name: typing_extensions___Literal[u'value', b'value']) -> builtin___bool:
            ...

        def ClearField(self, field_name: typing_extensions___Literal[u'key', b'key', u'value', b'value']) -> None:
            ...
    type___SecurityRequirementEntry = SecurityRequirementEntry

    @property
    def security_requirement(self) -> google___protobuf___internal___containers___MessageMap[typing___Text, type___SecurityRequirement.SecurityRequirementValue]:
        ...

    def __init__(self, *, security_requirement: typing___Optional[typing___Mapping[typing___Text, type___SecurityRequirement.SecurityRequirementValue]]=None) -> None:
        ...

    def ClearField(self, field_name: typing_extensions___Literal[u'security_requirement', b'security_requirement']) -> None:
        ...
type___SecurityRequirement = SecurityRequirement

class Scopes(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...

    class ScopeEntry(google___protobuf___message___Message):
        DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
        key: typing___Text = ...
        value: typing___Text = ...

        def __init__(self, *, key: typing___Optional[typing___Text]=None, value: typing___Optional[typing___Text]=None) -> None:
            ...

        def ClearField(self, field_name: typing_extensions___Literal[u'key', b'key', u'value', b'value']) -> None:
            ...
    type___ScopeEntry = ScopeEntry

    @property
    def scope(self) -> google___protobuf___internal___containers___ScalarMap[typing___Text, typing___Text]:
        ...

    def __init__(self, *, scope: typing___Optional[typing___Mapping[typing___Text, typing___Text]]=None) -> None:
        ...

    def ClearField(self, field_name: typing_extensions___Literal[u'scope', b'scope']) -> None:
        ...
type___Scopes = Scopes
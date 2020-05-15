# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: gtfs-realtime-transiter-extension.proto

import sys

_b = sys.version_info[0] < 3 and (lambda x: x) or (lambda x: x.encode("latin1"))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import gtfs_realtime_pb2 as gtfs__realtime__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
    name="gtfs-realtime-transiter-extension.proto",
    package="transit_realtime",
    syntax="proto2",
    serialized_options=None,
    serialized_pb=_b(
        '\n\'gtfs-realtime-transiter-extension.proto\x12\x10transit_realtime\x1a\x13gtfs-realtime.proto"\xa4\x01\n\x1cStopTimeUpdateAdditionalData\x12\r\n\x05track\x18\x01 \x01(\t2u\n\x0f\x61\x64\x64itional_data\x12+.transit_realtime.TripUpdate.StopTimeUpdate\x18\xc1\r \x01(\x0b\x32..transit_realtime.StopTimeUpdateAdditionalData"\xab\x01\n\x13\x41lertAdditionalData\x12\x12\n\ncreated_at\x18\x01 \x01(\x04\x12\x12\n\nupdated_at\x18\x02 \x01(\x04\x12\x12\n\nsort_order\x18\x03 \x01(\x04\x32X\n\x0f\x61\x64\x64itional_data\x12\x17.transit_realtime.Alert\x18\xc1\r \x01(\x0b\x32%.transit_realtime.AlertAdditionalData'
    ),
    dependencies=[gtfs__realtime__pb2.DESCRIPTOR,],
)


_STOPTIMEUPDATEADDITIONALDATA = _descriptor.Descriptor(
    name="StopTimeUpdateAdditionalData",
    full_name="transit_realtime.StopTimeUpdateAdditionalData",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="track",
            full_name="transit_realtime.StopTimeUpdateAdditionalData.track",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
    ],
    extensions=[
        _descriptor.FieldDescriptor(
            name="additional_data",
            full_name="transit_realtime.StopTimeUpdateAdditionalData.additional_data",
            index=0,
            number=1729,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=True,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
    ],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto2",
    extension_ranges=[],
    oneofs=[],
    serialized_start=83,
    serialized_end=247,
)


_ALERTADDITIONALDATA = _descriptor.Descriptor(
    name="AlertAdditionalData",
    full_name="transit_realtime.AlertAdditionalData",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="created_at",
            full_name="transit_realtime.AlertAdditionalData.created_at",
            index=0,
            number=1,
            type=4,
            cpp_type=4,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="updated_at",
            full_name="transit_realtime.AlertAdditionalData.updated_at",
            index=1,
            number=2,
            type=4,
            cpp_type=4,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="sort_order",
            full_name="transit_realtime.AlertAdditionalData.sort_order",
            index=2,
            number=3,
            type=4,
            cpp_type=4,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
    ],
    extensions=[
        _descriptor.FieldDescriptor(
            name="additional_data",
            full_name="transit_realtime.AlertAdditionalData.additional_data",
            index=0,
            number=1729,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=True,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
    ],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto2",
    extension_ranges=[],
    oneofs=[],
    serialized_start=250,
    serialized_end=421,
)

DESCRIPTOR.message_types_by_name[
    "StopTimeUpdateAdditionalData"
] = _STOPTIMEUPDATEADDITIONALDATA
DESCRIPTOR.message_types_by_name["AlertAdditionalData"] = _ALERTADDITIONALDATA
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

StopTimeUpdateAdditionalData = _reflection.GeneratedProtocolMessageType(
    "StopTimeUpdateAdditionalData",
    (_message.Message,),
    dict(
        DESCRIPTOR=_STOPTIMEUPDATEADDITIONALDATA,
        __module__="gtfs_realtime_transiter_extension_pb2"
        # @@protoc_insertion_point(class_scope:transit_realtime.StopTimeUpdateAdditionalData)
    ),
)
_sym_db.RegisterMessage(StopTimeUpdateAdditionalData)

AlertAdditionalData = _reflection.GeneratedProtocolMessageType(
    "AlertAdditionalData",
    (_message.Message,),
    dict(
        DESCRIPTOR=_ALERTADDITIONALDATA,
        __module__="gtfs_realtime_transiter_extension_pb2"
        # @@protoc_insertion_point(class_scope:transit_realtime.AlertAdditionalData)
    ),
)
_sym_db.RegisterMessage(AlertAdditionalData)

_STOPTIMEUPDATEADDITIONALDATA.extensions_by_name[
    "additional_data"
].message_type = _STOPTIMEUPDATEADDITIONALDATA
gtfs__realtime__pb2.TripUpdate.StopTimeUpdate.RegisterExtension(
    _STOPTIMEUPDATEADDITIONALDATA.extensions_by_name["additional_data"]
)
_ALERTADDITIONALDATA.extensions_by_name[
    "additional_data"
].message_type = _ALERTADDITIONALDATA
gtfs__realtime__pb2.Alert.RegisterExtension(
    _ALERTADDITIONALDATA.extensions_by_name["additional_data"]
)

# @@protoc_insertion_point(module_scope)

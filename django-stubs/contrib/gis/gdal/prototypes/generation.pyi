from ctypes import c_char_p
from typing import Any, Optional

class gdal_char_p(c_char_p): ...

def bool_output(func: Any, argtypes: Any, errcheck: Optional[Any] = ...): ...
def double_output(
    func: Any, argtypes: Any, errcheck: bool = ..., strarg: bool = ..., cpl: bool = ...
): ...
def geom_output(func: Any, argtypes: Any, offset: Optional[Any] = ...): ...
def int_output(func: Any, argtypes: Any, errcheck: Optional[Any] = ...): ...
def int64_output(func: Any, argtypes: Any): ...
def srs_output(func: Any, argtypes: Any): ...
def const_string_output(
    func: Any,
    argtypes: Any,
    offset: Optional[Any] = ...,
    decoding: Optional[Any] = ...,
    cpl: bool = ...,
): ...
def string_output(
    func: Any,
    argtypes: Any,
    offset: int = ...,
    str_result: bool = ...,
    decoding: Optional[Any] = ...,
): ...
def void_output(func: Any, argtypes: Any, errcheck: bool = ..., cpl: bool = ...): ...
def voidptr_output(func: Any, argtypes: Any, errcheck: bool = ...): ...
def chararray_output(func: Any, argtypes: Any, errcheck: bool = ...): ...

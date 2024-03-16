#!/usr/bin/env python3
""" Safely get value """

from typing import Mapping, Any, Union

Res = Union[Any, None]
D = Union[Any, None]


def safely_get_value(dct: Mapping[Any, Any], key: Any, default: D = None) -> Res:
    """ Return the value of a key in a dictionary or the default value"""
    if key in dct:
        return dct[key]
    else:
        return default

#!/usr/bin/env python3
"""
Module Name: 101-safely_get_value.py

Function:
---------
safely_get_value(dct: Mapping, key: Any, default: Union[T, None] = None) \
    -> Union[Any, T]
A function that returns a value from a mapping using a key.

"""
from typing import Union, Mapping, TypeVar, Any

T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any, default: Union[T, None] = None) \
                     -> Union[Any, T]:
    """
    A function that returns a value from a mapping using a key.

    parameters:
    - dct (Mapping): The mapping where a value will be retrieved from.
    - key (Any): The key used to look up in the mapping.
    - default (Union[T, None]): The default value to return.

    Returns:
    - Union[Any, T]: The value associated with the key else the default.
    """
    if key in dct:
        return dct[key]
    else:
        return default

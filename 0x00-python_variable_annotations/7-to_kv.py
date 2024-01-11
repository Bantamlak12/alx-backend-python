#!/usr/bin/env python3
"""A module with complex types - string and int/float to tuple"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    A function that returns a tuple.

    parameters:
    - k (str): A string
    - v (Union[int, float]): Integer or float value.

    Returns:
    - A tuple with a string and float.
    """
    return (k, v ** 2)

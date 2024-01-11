#!/usr/bin/env python3
"""A module that returns the fist element of a sequence"""
from typing import Sequence, Any, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    A function that returns the first element of a sequence.

    paramenters:
    - lst (lst: Sequence[Any]): A sequence where the first element is to be
    retrieved.

    Returns:
    - Union[Any, NoneType]: The first element of the sequence if it does exist,
    else return None
    """
    if lst:
        return lst[0]
    else:
        return None

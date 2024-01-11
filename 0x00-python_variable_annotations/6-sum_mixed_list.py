#!/usr/bin/env python3
"""A module that takes a mixed list and returns their sum as a float."""
from typing import Union, List


Num = Union[int, float]


def sum_mixed_list(mxd_lst: List[Num]) -> float:
    """
    A function that returns a sum as a float.

    parameters:
    - mxd_lst (List[Num]): List of integers and flaots.

    Returns:
    - Their sum as a float.
    """
    sum = 0
    for num in mxd_lst:
        sum += num
    return sum

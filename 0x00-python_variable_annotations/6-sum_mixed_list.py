#!/usr/bin/env python3
"""A module that takes a mixed list and returns their sum as a float."""
from typing import Union, List


Num = Union[int, float]


def sum_mixed_list(mxd_lst: List[Num]) -> float:
    """ A type-annotated function `sum_mixed_list` which takes a list `mxd_lst`
        of integers and floats and returns their sum as a float.
    """
    sum = 0
    for num in mxd_lst:
        sum += num
    return sum

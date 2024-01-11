#!/usr/bin/env python3
"""A module that takes a list of floats and returns their sum as a float."""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """ It takes a list `input_list` of floats as argument and
        returns their sum as a float.
    """
    sum = 0
    for num in input_list:
        sum += num
    return sum

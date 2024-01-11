#!/usr/bin/env python3
"""A module that takes a list of floats and returns their sum as a float."""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    A function that returns the sum as a float.

    parameters:
    - input_list (List[float]): List of floating numbers.

    Returns:
    - Their sum as a float.
    """
    sum = 0
    for num in input_list:
        sum += num
    return sum

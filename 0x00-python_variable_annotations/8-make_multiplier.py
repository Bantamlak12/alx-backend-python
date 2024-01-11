#!/usr/bin/env python3
"""A module that returns a multiplier function"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Creates a function that multiplies a float by a multiplier.

    parameters:
    - multiplier (float): The multiplier to be used in the return function.

    Returns:
    - Callable[[float], float]: A function that takes a float as input and
        returns the result.
    """
    def multiplier_fun(x: float) -> float:
        return x * multiplier
    return multiplier_fun

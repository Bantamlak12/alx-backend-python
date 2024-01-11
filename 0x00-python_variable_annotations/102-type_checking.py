#!/usr/bin/env python3
"""
Module Name: 102-type_checking.py

Function:
--------
zoom_array(lst: Tuple, factor: int = 2) -> List

"""
from typing import Tuple, List


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """
    A function that zooms-in an array by repeating the elements.

    parameters:
    - lst (Tuple): The tuple to be zoomed in.
    - factor (int, optional): The number of times each element
    should be repeated.

    Returns:
    - List: The zoomed-in list
    """
    zoomed_in: List = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in


array = (12, 72, 91)

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)

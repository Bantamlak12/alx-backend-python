#!/usr/bin/env python3
"""A module that type an iterable"""
from typing import Iterable, List, Tuple, Sequence


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    A function that takes an iterable of sequence and returns
    list of tuples.

    parameters:
    - lst (Iterable[Sequence]): Iterable containg the sequence.

    Returns:
    - List[Tuple[Sequence, int]]: A list of tuples where each tuple contains
    a sequence.
    """
    return [(i, len(i)) for i in lst]

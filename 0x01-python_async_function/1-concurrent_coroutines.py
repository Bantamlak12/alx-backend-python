#!/usr/bin/env python3
"""
File: 1-concurrent_coroutines.py

Function:
---------
A file that return all the delays.
"""
import asyncio
from typing import List


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    parameters:
    - n (int): The number of times wait_random() will be called.
    - max_delay (int): A second to delay

    Returns:
    - (float): List of all delays.
    """
    return sorted([await wait_random(max_delay) for i in range(n)])

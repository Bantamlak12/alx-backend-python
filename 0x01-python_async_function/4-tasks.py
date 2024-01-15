#!/usr/bin/env python3
"""
File: 4-tasks.py
"""
import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    parameters:
    - n (int): The number of times wait_random() will be called.
    - max_delay (int): A second to delay

    Returns:
    - (float): List of all delays.
    """
    return sorted([await task_wait_random(max_delay) for i in range(n)])

#!/usr/bin/env python3
"""
File: 1-async_comprehension.py

Async Comprehensions
"""
from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    Collects 10 random numbers using an async comprehensing
    and returns it.

    Returns:
    - List[float]: 10 random numbers
    """
    return [i async for i in async_generator()]

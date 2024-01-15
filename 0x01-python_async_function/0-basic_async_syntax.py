#!/usr/bin/env python3
"""
File: 0-basic_async_syntax.py
"""
import asyncio
import random
from typing import Union


async def wait_random(max_delay: int = 10) -> float:
    """
    Parameters:
    - max_delay=10 (number) - maximum seconds to delay

    Returns:
    - waits for a random delay and returns it.
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay

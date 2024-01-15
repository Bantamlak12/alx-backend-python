#!/usr/bin/env python3
"""
File: 0-basic_async_syntax.py
"""
import asyncio
import random


async def wait_random(max_delay=10):
    """
    Parameters:
    - max_delay=10 (number) - maximum seconds to delay

    Returns:
    - waits for a random delay and returns it.
    """
    return random.uniform(0, max_delay)

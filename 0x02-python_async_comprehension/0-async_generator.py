#!/usr/bin/env python3
"""
File: 0-async_generator.py

Async Generator
"""
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """
    Generator[float, None, None]: The generator yields floats and doesn't take
    any parameter or return any result.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)

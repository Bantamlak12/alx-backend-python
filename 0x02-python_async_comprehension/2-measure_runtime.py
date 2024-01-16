#!/usr/bin/env python3
"""
File: 2-measure_runtime.py

Run time for four parallel comprehensions
"""
import asyncio
import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Execute async_comprehension four times in parallel using asyncio.gather

    Returns:
    - (float): The total run time
    """
    start_time = time.time()
    await asyncio.gather(*[async_comprehension() for _ in range(4)])
    end_time = time.time()
    total_run_time = end_time - start_time

    return total_run_time

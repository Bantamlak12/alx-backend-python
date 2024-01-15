#!/usr/bin/env python3
"""
File: 2-measure_runtime.py

Function:
---------
A file that calculate total elapsed time.
"""
import asyncio
import time

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    parameters:
    - n (int): The number of times wait_random() will be called.
    - max_delay (int): A second to delay

    Returns:
    - The elapsed time
    """
    start_time = time.time()

    asyncio.run(wait_n(n, max_delay))
    end_time = time.time()

    elapsed_time = end_time - start_time

    return elapsed_time / n

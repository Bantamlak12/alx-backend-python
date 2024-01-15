#!/usr/bin/env python3
"""
File: 3-tasks.py

A file that takes an integer `max_delay` and returns a asyncio.Task
"""
import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    parameters:
    - max_delay (int): Maximum number of delay

    Returns:
    - A asyncio.Task
    """
    return asyncio.create_task(wait_random(max_delay))

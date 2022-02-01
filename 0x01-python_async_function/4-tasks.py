#!/usr/bin/env python3
"""
Module for 4. Tasks.
0x01. Python - Async
"""
import asyncio
from typing import List


task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    executes multiples coroutines at the same time
    parameters n : int
    max_delay : int
    Returns List[float]
    list of the delays in ascending order
    """
    tasks = [task_wait_random(max_delay) for i in range(n)]
    return [await task for task in asyncio.as_completed(tasks)]

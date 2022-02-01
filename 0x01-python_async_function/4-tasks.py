#!/usr/bin/env python3
"""
Module for 4. Tasks.
0x01. Python - Async
"""
import asyncio
import random
from typing import List


task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int = 0, max_delay: int = 10) -> List[float]:
    """
    executes multiples coroutines at the same time
    parameters n : int
    max_delay : int
    Returns List[float]
    list of the delays in ascending order
    """
    delays: List[float] = []
    tasks: List[asyncio.Task] = []

    for _ in range(n):
        tasks.append(task_wait_random(max_delay))

    for task in asyncio.as_completed((tasks)):
        delay = await task
        delays.append(delay)

    return delays

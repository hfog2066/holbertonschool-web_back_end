#!/usr/bin/env python3
"""
Module for 0. Async Generator.
0x02. Python - Async Comprehension
"""

import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """
    Asynchronous generator random numbers from 0 to 10.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)

#!/usr/bin/env python3
"""
Module for async basics.
"""

from typing import List
import bisect
import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Function that wait randomly between 0 and max_delay.
    """
    tasks = [wait_random(max_delay) for _ in range(n)]
    delays: List[float] = []

    for i in asyncio.as_completed(tasks):
        delay = await i
        bisect.insort(delays, delay)

    return delays

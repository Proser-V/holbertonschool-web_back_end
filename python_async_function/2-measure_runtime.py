#!/usr/bin/env python3
"""
Module for async basics.
"""

import time
import asyncio


wait_n = __import__('1-concurrent_coroutines').wait_n


async def measure_time(n: int, max_delay: int) -> float:
    """
    Function that give the time delay.
    """
    return await time(wait_n(n, max_delay))

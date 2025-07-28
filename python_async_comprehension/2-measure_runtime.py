#!/usr/bin/env python3
"""
A module for a method.

With 2 lines doc.
"""
async_comprehension = __import__('0-async_generator').async_comprehension

import time
import asyncio


async def measure_runtime() -> float:
    """
    Said method.

    With 2 lines doc.
    """
    start = time.perf_counter()
    await asyncio.gather(
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
    )
    end = time.perf_counter()
    return end - start
#!/usr/bin/env python3

"""
A module for a method.
"""

import asyncio
import random
from typing import AsyncIterator


async def async_generator() -> AsyncIterator[float]:
    """
    The said method.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)

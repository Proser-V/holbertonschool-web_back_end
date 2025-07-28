#!/usr/bin/env python3
"""
A module for a method.
"""

import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    """
    The said method.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        val: float = random.uniform(0, 10)
        yield val

#!/usr/bin/env python3
"""
A module for a method.

With 2 lines doc.
"""

import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    """
    Said method.

    With 2 lines doc.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)

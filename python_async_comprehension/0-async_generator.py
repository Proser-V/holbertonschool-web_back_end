#!/usr/bin/env python3

"""
A module for a method.
"""

import asyncio
import random

async def async_generator():
    for _ in range(10):
        await asyncio.sleep(1)
        number = random(0, 10)
    return number

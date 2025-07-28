#!/usr/bin/env python3
"""
A module for a method.

With 2 lines doc.
"""
async_generator = __import__('0-async_generator').async_generator

from typing import List


async def async_comprehension() -> List[float]:
    """
    Said method.

    With 2 lines doc.
    """
    return [i async for i in async_generator()]
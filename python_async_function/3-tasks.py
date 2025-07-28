#!/usr/bin/env python3
"""
Module for async basics.
"""

import asyncio


wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Function that give the time delay.
    """
    return asyncio.run(wait_random(max_delay))

#!/usr/bin/env python3
"""
Module for async basics.
"""

from typing import List
import bisect

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Function that wait randomly between 0 and max_delay.
    """
    mylist = []
    for i in n:
        mylist.append(wait_random(max_delay))
    bisect.insort(mylist, i)
    return mylist

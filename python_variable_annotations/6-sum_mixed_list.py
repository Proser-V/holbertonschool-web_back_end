#!/usr/bin/env python3
"""
A module for a type-annotated function sum_mixed_list which takes a list
mxd_lst of integers and floats and returns their sum as a float.
"""

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Type-annotated function sum_mixed_list which takes a list mxd_lst of
    integers and floats and returns their sum as a float.
    """
    result: float = 0.00

    for i in mxd_lst:
        result += i
    return result

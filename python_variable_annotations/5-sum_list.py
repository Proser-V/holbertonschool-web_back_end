#!/usr/bin/env python3
"""
A module for a type-annotated function sum_list which takes a list input_list
of floats as argument and returns their sum as a float.
"""


def sum_list(input_list: list[float]) -> float:
    """
    Type-annotated function sum_list which takes a list input_list of floats
    as argument and returns their sum as a float.
    """
    result: float = 0.00

    for i in input_list:
        result += i
    return result

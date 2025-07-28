#!/usr/bin/env python3
"""
A module for a type-annotated function safely_get_value witch takes a dict of
variable type keys.
"""

from typing import TypeVar, Any, Dict

T = TypeVar('T')


def safely_get_value(dct: Dict[Any, T], key: Any, default: T = None) -> T:
    """
    A type-annotated function safely_get_value witch takes a dict of
    variable type keys.
    """
    if key in dct:
        return dct[key]
    else:
        return default

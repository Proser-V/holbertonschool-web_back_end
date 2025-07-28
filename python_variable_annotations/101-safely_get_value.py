#!/usr/bin/env python3
"""
A module for a type-annotated function safely_get_value witch takes a dict of
variable type keys.
"""

from typing import Dict, TypeVar


def safely_get_value(dct: Dict, key: TypeVar, default = None) -> Dict:
    """
    A type-annotated function safely_get_value witch takes a dict of
    variable type keys.
    """
    if key in dct:
        return dct[key]
    else:
        return default

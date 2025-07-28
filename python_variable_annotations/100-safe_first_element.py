#!/usr/bin/env python3
"""
A module for a type-annotated function safely_get_value witch takes a dict of
variable type keys.
"""

from typing import List, Any


def safe_first_element(lst: List) -> Any:
    """
    A type-annotated function safely_get_value witch takes a dict of
    variable type keys.
    """
    if lst:
        return lst[0]
    else:
        return None
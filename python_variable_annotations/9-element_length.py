#!/usr/bin/env python3
"""
A module for a type-annotated function element_length witch takes a list of
sequences.
"""

from typing import Tuple, List, Sequence


def element_length(lst: List[Sequence]) -> Tuple[Sequence, int]:
    """
    A type-annotated function element_length witch takes a list of
    sequences.
    """
    return [(i, len(i)) for i in lst]

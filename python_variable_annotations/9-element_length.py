#!/usr/bin/env python3
"""
A module for a type-annotated function element_length witch takes an iterable
of sequences.
"""

from typing import Tuple, List, Sequence, Iterable


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    A type-annotated function element_length witch takes a list of
    sequences.
    """
    return [(i, len(i)) for i in lst]

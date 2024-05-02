#!/usr/bin/env python3
"""
Module to define a function to calculate the length of elements in a list.
"""

from typing import Iterable, Sequence, Tuple, List


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Calculate the length of elements in a list.

    Args:
        lst (Iterable[Sequence]): The input list.

    Returns:
        List[Tuple[Sequence, int]]: A list of tuples where the first element
        is an element from the input list and the second element is its length.
    """
    return [(i, len(i)) for i in lst]

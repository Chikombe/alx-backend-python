#!/usr/bin/env python3
"""
Module to define a function to safely retrieve the first element of a list.
"""

from typing import Sequence, Any, Union


def safe_first_element(lst: Sequence) -> Union[Any, None]:
    """
    Safely retrieve the first element of a list.

    Args:
        lst (Sequence): The input list.

    Returns:
        Union[Any, None]: The first element of the list,
        or None if the list is empty.
    """
    if lst:
        return lst[0]
    else:
        return None

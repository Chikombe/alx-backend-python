#!/usr/bin/env python3
"""
Module to define a function to convert a string and a number to a tuple.
"""

from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Convert a string and a number to a tuple.

    Args:
        k (str): The string.
        v (Union[int, float]): The number.

    Returns:
        Tuple[str, float]: The tuple with string k
        and the square of int/float v.
    """
    return (k, v ** 2)

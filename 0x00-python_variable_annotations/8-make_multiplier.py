#!/usr/bin/env python3
"""
Module to define a function to create a multiplier function.
"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Create a multiplier function.

    Args:
        multiplier (float): The multiplier value.

    Returns:
        Callable[[float], float]: A function that multiplies
        a float by multiplier.
    """
    def multiplier_function(x: float) -> float:
        """
        Multiply a float by multiplier.

        Args:
            x (float): The input number.

        Returns:
            float: The result of multiplying x by multiplier.
        """
        return x * multiplier

    return multiplier_function

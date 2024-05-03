#!/usr/bin/env python3

from typing import Mapping, Any, Union, TypeVar

V = TypeVar('V')


def safely_get_value(dct: Mapping[Any, V], key: Any, default:
                     Union[V, None] = None) -> Union[V, None]:
    """
    Safely retrieve a value from a dictionary.

    Args:
        dct (Mapping[Any, V]): The dictionary to search.
        key (Any): The key to search for.
        default (Union[V, None], optional):
        The default value to return if the key is not found. Defaults to None.

    Returns:
        Union[V, None]: The value corresponding to the key, or
        the default value if the key is not found.
    """
    if key in dct:
        return dct[key]
    else:
        return default

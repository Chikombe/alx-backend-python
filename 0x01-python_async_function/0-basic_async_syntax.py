#!/usr/bin/env python3
"""  Basics of async """
import asyncio
import random
from typing import Union


async def wait_random(max_delay: int = 10) -> Union[float, int]:
    """Asynchronous coroutine that waits for a random delay between 0
    and max_delay seconds (inclusive) and returns it.

    Args:
        max_delay (int, optional): The maximum delay in seconds.
        Defaults to 10.

    Returns:
        Union[float, int]: The random delay.
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay

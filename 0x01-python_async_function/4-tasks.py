#!/usr/bin/env python3
""" Tasks """
import asyncio
from typing import List


def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Function that spawns task_wait_random n times
    with the specified max_delay.

    Args:
        n (int): The number of times to spawn task_wait_random.
        max_delay (int): The maximum delay in seconds for
        each task_wait_random call.

    Returns:
        List[float]: The list of delays in ascending order.
    """
    loop = asyncio.get_event_loop()
    tasks = [loop.create_task(task_wait_random(max_delay)) for _ in range(n)]
    delays = [await task for task in asyncio.as_completed(tasks)]
    return sorted(delays)

#!/usr/bin/env python3
"""Tasks """
import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """Regular function that creates and returns an asyncio.
    Task for wait_random.

    Args:
        max_delay (int): The maximum delay in seconds.

    Returns:
        asyncio.Task: An asyncio.Task object.
    """
    loop = asyncio.get_event_loop()
    return loop.create_task(wait_random(max_delay))

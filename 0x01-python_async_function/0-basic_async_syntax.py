#!/usr/bin/env python3
"""
Write an asynchronous coroutine
"""
import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    """
    Asynchronously waits for a random amount of time.

    Args:
        max_delay (float): The maximum delay in seconds (default is 10).

    Returns:
        float: The actual delay in seconds.

    """
    if max_delay < 0:
        raise ValueError("max_delay must be a positive number")

    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)

    return delay

#!/usr/bin/env python3
"""
measure_runtime
"""
import time
async_comprehension = __import__("1-async_comprehension")\
    .async_comprehension


async def measure_runtime() -> float:
    """
    Measure the runtime of the `async_comprehension` function.

    Returns:
        float: The runtime of the `async_comprehension` function in seconds.
    """
    start = time.perf_counter()
    await async_comprehension()
    end = time.perf_counter()

    return end - start

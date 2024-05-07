#!/usr/bin/env python3
"""
async_generator
"""
from typing import Generator
import asyncio
import random


async def async_generator() -> Generator[float, None, None]:
    """
    This is an async generator function that yields random
    float numbers between 0 and 10.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)

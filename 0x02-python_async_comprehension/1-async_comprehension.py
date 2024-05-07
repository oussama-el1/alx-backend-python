#!/usr/bin/env python3
"""
async_comprehension
"""
from typing import List


async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    This function asynchronously generates a list of floats using
    an async generator.
    """
    numbers = [number async for number in async_generator()]
    return numbers

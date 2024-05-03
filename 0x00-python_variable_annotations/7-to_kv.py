#!/usr/bin/env python3
""" create  type-annotated function to_kv """
from typing import Union, Tuple, Any


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """to_kv take a str and v can be int or float : tuple"""
    mytuple = (k, v ** 2)
    return mytuple

#!/usr/bin/env python3
""" function sum_list"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """ sum_list take """
    r: float = 0
    for num in input_list:
        r = r + num
    return r

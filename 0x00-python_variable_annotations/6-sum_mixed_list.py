#!/usr/bin/env python3
"""sum_mixed_list function"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    r: float = 0.0
    for value in mxd_lst:
        r = r + value
    return r

#!/usr/bin/env python3
""" zoom_array """
from typing import Tuple, List


def zoom_array(lst: List, factor: int = 2) -> List:
    """ solve zoom_array Types """
    zoomed_in: List = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in


array: List = [12, 72, 91]

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)

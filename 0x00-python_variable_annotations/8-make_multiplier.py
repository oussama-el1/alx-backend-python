#!/usr/bin/env python3
""" function make_multiplier """
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """ return a Callable[[float], float] """
    def fun(m: float):
        """ inner_function """
        return m * multiplier
    return fun

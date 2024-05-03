#!/usr/bin/env python3
""" Annotate the element_length function """
from typing import Iterable, List, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """ element_length return list of tuples with item and its len """
    return [(i, len(i)) for i in lst]

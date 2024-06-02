#!/usr/bin/env python3
"""Duck-typed annotations """
from typing import List, Tuple


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """Return a zoomed array"""
    zoomed: List = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed


array = (12, 72, 91)

zoom_two = zoom_array(array)

zoom_three = zoom_array(array, 3)

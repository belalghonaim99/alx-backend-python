#!/usr/bin/env python3
""" Basic annotations - make multiplier
Return a function that multiplies a float by another float
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """ Return a function that multiplies a float by another float"""
    def multiply(n: float) -> float:
        """ Return a function that multiplies a float by another float"""
        return n * multiplier
    return multiply

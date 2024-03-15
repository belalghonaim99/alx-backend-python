#!/usr/bin/env python3
""" Basic annotations - mixed list
Return the sum of a list of floats and integers
"""

from typing import Union, List


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """ Return the sum of a list of floats and integers"""
    return sum(mxd_lst)

#!/usr/bin/env python3
""" Basic annotations - length of a sequence
"""
from typing import Iterable, list, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> list[Tuple[Sequence, int]]:
    """ Return the length of a sequence"""
    return [(i, len(i)) for i in lst]

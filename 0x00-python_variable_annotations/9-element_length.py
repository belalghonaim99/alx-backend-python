#!/usr/bin/env python3
""" Basic annotations - length of a sequence
"""
from typing import Iterable, List, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """ Return the length of a sequence"""
    return [(i, len(i)) for i in lst]

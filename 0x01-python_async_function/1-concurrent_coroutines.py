#!/usr/bin/env python3

import asyncio
from typing import List


delay = __import__('0-basic_async_syntax').wait_random

async def wait_n(n: int, max_delay: int) -> List[float]:
    """Asynchronous coroutine that takes in an integer argument (n) and a"""
    """integer argument (max_delay, with a default value of 10) named"""
    delays = [delay(max_delay) for _ in range(n)]
    return [await delay for delay in asyncio.as_completed(delays)]
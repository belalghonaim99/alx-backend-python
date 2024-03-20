#!/usr/bin/env python3

import asyncio
import random

async def async_generator() -> None:
    """ Coroutine that loops 10 times, each time yielding a random number """
    for i in range(10):
        yield random.uniform(0, 10)
        await asyncio.sleep(1)
#!/usr/bin/env python3
""" 2. Run time for four parallel comprehensions  """
import asyncio

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def main():
    print(await async_comprehension())

asyncio.run(main())

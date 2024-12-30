import asyncio
from typing import Coroutine


async def limit_execution_time(coro: Coroutine, max_execution_time: float) -> None:
    async with asyncio.timeout(max_execution_time):
        await coro


async def limit_execution_time_many(*coros: Coroutine, max_execution_time: float) -> None:
    tasks = [asyncio.create_task(coro) for coro in coros]
    _, pending = await asyncio.wait(tasks, timeout=max_execution_time)

    for t in pending:
        t.cancel()

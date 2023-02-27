import asyncio
from typing import Any, List


async def async_executor(executions_per_second: int, to_execute: List[Any]):
    while to_execute:
        await asyncio.gather(*to_execute[:executions_per_second])
        del to_execute[:executions_per_second]
        await asyncio.sleep(1)

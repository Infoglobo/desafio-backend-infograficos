from abc import ABC, abstractmethod
from typing import Generic, List, TypeVar

import httpx

from infografia_admin.job.app.interfaces.command import AsyncCommand

T = TypeVar("T")


class BaseCommandRequest(AsyncCommand[T], ABC, Generic[T]):
    async def execute(self) -> T | None:
        async with httpx.AsyncClient() as client:
            response = await self.request(client)
        if response and response.status_code == 200:
            return await self.build_dto(response.json())
        return None

    @abstractmethod
    async def build_dto(self, data: dict | List[dict]) -> T:
        ...

    @abstractmethod
    async def request(self, client: httpx.AsyncClient) -> httpx.Response:
        ...

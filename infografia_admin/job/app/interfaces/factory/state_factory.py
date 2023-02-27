from abc import ABC, abstractmethod
from typing import List

from infografia_admin.job.app.dto.state import StateDto
from infografia_admin.job.app.interfaces.entities.state import IState


class IStateFactory(ABC):
    @abstractmethod
    async def manufacture_from_dto(self, dto: StateDto) -> IState:
        ...

    @abstractmethod
    async def bulk_manufacture_from_dto(self, dtos: List[StateDto]) -> List[IState]:
        ...

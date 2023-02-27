from abc import ABC, abstractmethod
from typing import List
from infografia_admin.job.app.dto.city import CityDto
from infografia_admin.job.app.dto.state import StateDto

from infografia_admin.job.app.interfaces.command import AsyncCommand


class IIbge(ABC):
    @abstractmethod
    def list_states(self) -> AsyncCommand[List[StateDto] | None]:
        ...

    @abstractmethod
    def list_cities_by_state(
        self, state_acronym: str
    ) -> AsyncCommand[List[CityDto] | None]:
        ...

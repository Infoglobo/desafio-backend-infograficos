from abc import ABC, abstractmethod
from infografia_admin.job.app.dto.state import StateDto
from infografia_admin.job.app.interfaces.builder.state_builder import IStateBuilder

from infografia_admin.job.app.interfaces.entities.city import ICity


class IState(ABC):
    cities: dict[str, ICity]

    @property
    @abstractmethod
    def builder(self) -> IStateBuilder:
        ...

    @property
    @abstractmethod
    def info(self) -> StateDto:
        ...

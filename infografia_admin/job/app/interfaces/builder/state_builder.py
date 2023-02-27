from abc import ABC, abstractmethod

from infografia_admin.job.app.interfaces.entities.city import ICity


class IStateBuilder(ABC):
    @abstractmethod
    async def build_cities(self) -> dict[str, ICity]:
        ...

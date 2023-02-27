from abc import ABC, abstractmethod
from infografia_admin.job.app.dto.city import CityDto
from infografia_admin.job.app.dto.weather import WeatherDto
from infografia_admin.job.app.interfaces.command import AsyncCommand


class ICity(ABC):
    @property
    @abstractmethod
    def weather(self) -> AsyncCommand[WeatherDto]:
        ...

    @property
    @abstractmethod
    def info(self) -> CityDto:
        ...

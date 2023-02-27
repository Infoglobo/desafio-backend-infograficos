from abc import ABC, abstractmethod
from infografia_admin.job.app.dto.city import CityCallbackDto, CityDto

from infografia_admin.job.app.dto.state import StateCallbackDto, StateDto
from infografia_admin.job.app.dto.weather import WeatherCallbackDto, WeatherDto
from infografia_admin.job.app.interfaces.command import AsyncCommand


class IAdminLocation(ABC):
    @abstractmethod
    def create_state(self, data: StateDto) -> AsyncCommand[StateCallbackDto]:
        ...

    @abstractmethod
    def create_city(self, data: CityDto) -> AsyncCommand[CityCallbackDto]:
        ...


class IAdminWeather(ABC):
    @abstractmethod
    def create_weather(
        self, data: AsyncCommand[WeatherDto]
    ) -> AsyncCommand[WeatherCallbackDto]:
        ...

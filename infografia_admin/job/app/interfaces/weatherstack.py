from abc import ABC, abstractmethod

from infografia_admin.job.app.dto.weather import WeatherDto
from infografia_admin.job.app.interfaces.command import AsyncCommand


class IWeatherStack(ABC):
    @abstractmethod
    def get_current_weather(self, city_name: str) -> AsyncCommand[WeatherDto]:
        ...

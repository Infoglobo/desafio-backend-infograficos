from infografia_admin.job.app.dto.weather import WeatherDto
from infografia_admin.job.app.interfaces.command import AsyncCommand
from infografia_admin.job.app.interfaces.weatherstack import IWeatherStack
from infografia_admin.job.infra.api.weatherstack.commands.get_current_weather import (
    GetCurrentWeatherByCity,
)


class WeatherStack(IWeatherStack):
    def get_current_weather(self, city_name: str) -> AsyncCommand[WeatherDto]:
        return GetCurrentWeatherByCity(city_name=city_name)

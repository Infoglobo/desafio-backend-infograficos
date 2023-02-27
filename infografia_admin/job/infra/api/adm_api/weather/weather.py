from infografia_admin.job.app.dto.weather import WeatherCallbackDto, WeatherDto
from infografia_admin.job.app.interfaces.admin_api import IAdminWeather
from infografia_admin.job.app.interfaces.command import AsyncCommand
from infografia_admin.job.infra.api.adm_api.weather.commands.create_weather import (
    CreateWeather,
)


class AdminWeather(IAdminWeather):
    def create_weather(
        self, data: AsyncCommand[WeatherDto]
    ) -> AsyncCommand[WeatherCallbackDto]:
        return CreateWeather(data=data)

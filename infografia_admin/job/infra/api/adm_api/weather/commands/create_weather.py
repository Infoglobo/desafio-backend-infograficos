from typing import List

import httpx
from loguru import logger
from infografia_admin.job.app.dto.weather import WeatherCallbackDto, WeatherDto
from infografia_admin.job.app.interfaces.command import AsyncCommand
from infografia_admin.job.infra.base.command import BaseCommandRequest
from infografia_admin.job.app.config.settings import Settings


class CreateWeather(BaseCommandRequest[WeatherCallbackDto]):
    def __init__(self, data: AsyncCommand[WeatherDto]) -> None:
        self.data = data

    async def build_dto(self, data: dict | List[dict]) -> WeatherCallbackDto:
        return WeatherCallbackDto(
            id=data.get("id"),
            temperature=data.get("temperature"),
            wind_speed=data.get("wind_speed"),
            wind_degree=data.get("wind_degree"),
            pressure=data.get("pressure"),
            precip=data.get("pressure"),
            humidity=data.get("humidity"),
            cloudcover=data.get("cloudcover"),
            feelslike=data.get("feelslike"),
            uv_index=data.get("uv_index"),
            city_name=data.get("city_name"),
            observation_time=data.get("observation_time"),
            wind_dir=data.get("wind_dir"),
        )

    async def request(self, client: httpx.AsyncClient) -> httpx.Response:
        self.data = await self.data.execute()
        logger.info(f"Inserting weather from {self.data.city_name} into Admin Api")
        response = await client.post(
            f"{Settings.admin_api_url}/api/v1/weather/", data=self.data.dict()
        )
        logger.info(
            f"Inserted weather from {self.data.city_name} into Admin Api - status code: {response.status_code} body: {response.json()}"  # pylint: disable=C0301
        )
        return response

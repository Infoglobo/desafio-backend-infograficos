from typing import List

import httpx
from loguru import logger

from infografia_admin.job.app.config.settings import Settings
from infografia_admin.job.app.dto.weather import WeatherDto
from infografia_admin.job.infra.base.command import BaseCommandRequest


class GetCurrentWeatherByCity(BaseCommandRequest[WeatherDto]):
    def __init__(self, city_name: str) -> None:
        self.city_name = city_name

    async def build_dto(self, data: dict | List[dict]) -> WeatherDto:
        current = data.get("current", {})
        return WeatherDto(
            temperature=current.get("temperature", 0),
            wind_speed=current.get("wind_speed", 0),
            wind_degree=current.get("wind_degree", 0),
            pressure=current.get("pressure", 0),
            precip=current.get("precip", 0),
            humidity=current.get("humidity", 0),
            cloudcover=current.get("cloudcover", 0),
            feelslike=current.get("feelslike", 0),
            uv_index=current.get("uv_index", 0),
            city_name=self.city_name,
            observation_time=current.get("observation_time", ""),
            wind_dir=current.get("wind_dir", ""),
        )

    async def request(self, client: httpx.AsyncClient) -> httpx.Response:
        logger.info(f"Getting weather from {self.city_name}")
        try:
            response = await client.get(
                f"{Settings.weatherstack_api_url}/current",
                params={
                    "access_key": Settings.weatherstack_api_token,
                    "query": self.city_name,
                },
            )
        except Exception as err:  # pylint: disable=W0718
            logger.error(
                f"An error occurred when Getting weather from {self.city_name} - error: {err}"
            )
            return None
        logger.info(
            f"Getted weather from {self.city_name} - status code: {response.status_code} body: {response.json()}"  # pylint: disable=C0301
        )
        return response

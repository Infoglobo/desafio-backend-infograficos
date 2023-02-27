from typing import List

import httpx
from loguru import logger

from infografia_admin.job.app.config.settings import Settings
from infografia_admin.job.app.dto.city import CityDto
from infografia_admin.job.infra.base.command import BaseCommandRequest


class ListCitysByState(BaseCommandRequest[List[CityDto]]):
    def __init__(self, state_acronym: str) -> None:
        super().__init__()
        self.state_acronym = state_acronym

    async def request(self, client: httpx.AsyncClient) -> httpx.Response:
        logger.info(f"Listing cities from {self.state_acronym} by ibge api")
        response = await client.get(
            f"{Settings.ibge_api_url}/api/v1/localidades/estados/{self.state_acronym}/distritos"
        )
        logger.info(
            f"Listed cities from {self.state_acronym} - status code: {response.status_code} body: {response.json()}"  # pylint: disable=C0301
        )
        return response

    async def build_dto(self, data: dict | List[dict]) -> List[CityDto]:
        return [
            CityDto(
                state_name=city.get("municipio", {})
                .get("microrregiao", {})
                .get("mesorregiao", {})
                .get("UF", {})
                .get("nome"),
                name=city.get("municipio", {}).get("nome"),
                microregion=city.get("municipio", {})
                .get("microrregiao", {})
                .get("nome"),
                mesoregion=city.get("municipio", {})
                .get("microrregiao", {})
                .get("mesorregiao", {})
                .get("nome"),
                immediate_region=city.get("municipio", {})
                .get("regiao-imediata", {})
                .get("nome"),
                middle_region=city.get("municipio", {})
                .get("regiao-imediata", {})
                .get("regiao-intermediaria", {})
                .get("nome"),
            )
            for city in data
        ]

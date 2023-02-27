from typing import Any, Coroutine, List

import httpx
from loguru import logger
from infografia_admin.job.app.config.settings import Settings
from infografia_admin.job.app.dto.city import CityCallbackDto, CityDto
from infografia_admin.job.infra.base.command import BaseCommandRequest


class CreateCity(BaseCommandRequest[CityCallbackDto]):
    def __init__(self, data: CityDto) -> None:
        super().__init__()
        self.data = data

    async def build_dto(
        self, data: dict | List[dict]
    ) -> Coroutine[Any, Any, CityCallbackDto]:
        return CityCallbackDto(
            id=data.get("id"),
            state_name=data.get("state_name"),
            name=data.get("name"),
            microregion=data.get("microregion"),
            mesoregion=data.get("mesoregion"),
            immediate_region=data.get("immediate_region"),
            middle_region=data.get("middle_region"),
        )

    async def request(
        self, client: httpx.AsyncClient
    ) -> Coroutine[Any, Any, httpx.Response]:
        logger.info(f"Inserting {self.data.name} city into Admin Api")
        response = await client.post(
            f"{Settings.admin_api_url}/api/v1/location/city", data=self.data.dict()
        )
        logger.info(
            f"Inserted {self.data.name} city into Admin Api - status code: {response.status_code} body: {response.json()}"  # pylint: disable=C0301
        )
        return response

from typing import List

import httpx
from loguru import logger
from infografia_admin.job.app.config.settings import Settings
from infografia_admin.job.app.dto.state import StateCallbackDto, StateDto
from infografia_admin.job.infra.base.command import BaseCommandRequest


class CreateState(BaseCommandRequest[StateCallbackDto]):
    def __init__(self, data: StateDto) -> None:
        super().__init__()
        self.data = data

    async def build_dto(self, data: dict | List[dict]) -> StateCallbackDto:
        return StateCallbackDto(
            id=data.get("id"),
            state_acronym=data.get("state_acronym"),
            state_name=data.get("state_name"),
            region_acronym=data.get("region_acronym"),
            region_name=data.get("region_name"),
        )

    async def request(self, client: httpx.AsyncClient) -> httpx.Response:
        logger.info(f"Inserting {self.data.state_name} state into Admin Api")
        response = await client.post(
            f"{Settings.admin_api_url}/api/v1/location/state", data=self.data.dict()
        )
        logger.info(
            f"inserted {self.data.state_name} state into Admin Api - status code: {response.status_code} body: {response.json()}"  # pylint: disable=C0301
        )
        return response

from typing import Any, Coroutine, List

import httpx
from loguru import logger
from infografia_admin.job.app.config.settings import Settings

from infografia_admin.job.app.dto.state import StateDto
from infografia_admin.job.infra.base.command import BaseCommandRequest


class ListStates(BaseCommandRequest[StateDto]):
    async def request(self, client: httpx.AsyncClient) -> httpx.Response:
        logger.info("Listing states by ibge api")
        response = await client.get(
            f"{Settings.ibge_api_url}/api/v1/localidades/estados"
        )
        logger.info(
            f"Listed states by ibge api - status code: {response.status_code} body: {response.json()}"
        )
        return response

    async def build_dto(
        self, data: dict | List[dict]
    ) -> Coroutine[Any, Any, List[StateDto]]:
        return [
            StateDto(
                state_acronym=state.get("sigla"),
                state_name=state.get("nome"),
                region_acronym=state.get("regiao", {}).get("sigla"),
                region_name=state.get("regiao", {}).get("nome"),
            )
            for state in data
        ]

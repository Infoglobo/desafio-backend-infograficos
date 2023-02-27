from infografia_admin.job.app.dto.city import CityCallbackDto, CityDto
from infografia_admin.job.app.dto.state import StateCallbackDto, StateDto
from infografia_admin.job.app.interfaces.admin_api import IAdminLocation
from infografia_admin.job.app.interfaces.command import AsyncCommand
from infografia_admin.job.infra.api.adm_api.location.commands.create_city import (
    CreateCity,
)
from infografia_admin.job.infra.api.adm_api.location.commands.create_state import (
    CreateState,
)


class AdminLocation(IAdminLocation):
    def create_state(self, data: StateDto) -> AsyncCommand[StateCallbackDto]:
        return CreateState(data)

    def create_city(self, data: CityDto) -> AsyncCommand[CityCallbackDto]:
        return CreateCity(data)

from infografia_admin.job.app.dto.city import CityDto
from infografia_admin.job.app.dto.state import StateDto
from infografia_admin.job.app.interfaces.command import AsyncCommand
from infografia_admin.job.infra.api.ibge.commands.list_city import ListCitysByState
from infografia_admin.job.infra.api.ibge.commands.list_state import ListStates


class Ibge:
    def list_states(self) -> AsyncCommand[StateDto]:
        return ListStates()

    def list_cities_by_state(self, state_acronym: str) -> AsyncCommand[CityDto]:
        return ListCitysByState(state_acronym)

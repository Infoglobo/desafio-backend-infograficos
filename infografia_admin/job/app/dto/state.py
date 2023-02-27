from pydantic import BaseModel


class StateDto(BaseModel):
    state_acronym: str
    state_name: str
    region_acronym: str
    region_name: str


class StateCallbackDto(BaseModel):
    id: int  # pylint: disable=C0103
    state_acronym: str
    state_name: str
    region_acronym: str
    region_name: str

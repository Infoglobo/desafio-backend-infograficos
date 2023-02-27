from pydantic import BaseModel


class CityDto(BaseModel):
    state_name: str | None
    name: str
    microregion: str
    mesoregion: str
    immediate_region: str
    middle_region: str


class CityCallbackDto(BaseModel):
    id: int  # pylint: disable=C0103
    state_name: str
    name: str
    microregion: str
    mesoregion: str
    immediate_region: str
    middle_region: str

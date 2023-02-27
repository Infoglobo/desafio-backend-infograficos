from pydantic import BaseModel  # pydantic: disable=E0611


class WeatherDto(BaseModel):
    temperature: int | None
    wind_speed: int | None
    wind_degree: int | None
    pressure: int | None
    precip: int | None
    humidity: int | None
    cloudcover: int | None
    feelslike: int | None
    uv_index: int | None
    city_name: str | None
    observation_time: str | None
    wind_dir: str | None


class WeatherCallbackDto(BaseModel):
    id: int | None  # pylint: disable=C0103
    temperature: int | None
    wind_speed: int | None
    wind_degree: int | None
    pressure: int | None
    precip: int | None
    humidity: int | None
    cloudcover: int | None
    feelslike: int | None
    uv_index: int | None
    city_name: str | None
    observation_time: str | None
    wind_dir: str | None

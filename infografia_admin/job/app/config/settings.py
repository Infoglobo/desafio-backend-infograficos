import os
from dotenv import load_dotenv


class Settings:
    ibge_api_url: str
    admin_api_url: str
    weatherstack_api_url: str
    weatherstack_api_token: str

    @staticmethod
    def load():
        load_dotenv()
        Settings.admin_api_url = os.getenv("ADMIN_API_URL")
        Settings.ibge_api_url = os.getenv("IBGE_API_URL")
        Settings.weatherstack_api_url = os.getenv("WEATHERSTACK_API_URL")
        Settings.weatherstack_api_token = os.getenv("WEATHERSTACK_API_TOKEN")

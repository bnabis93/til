from functools import lru_cache

from pydantic import BaseSettings
from starlette.config import Config


class AuthConfigs(BaseSettings):
    """Google Auth configs."""

    GOOGLE_CLIENT_ID: str
    GOOGLE_CLIENT_SECRET: str

    class Config:
        """Load from .env file."""

        env_file = ".env"


@lru_cache
def get_configs():
    """Get configs."""

    return Config(AuthConfigs.Config.env_file)


configs = get_configs()
# Open IDentification
GOOGLE_CONF_URL = "https://accounts.google.com/.well-known/openid-configuration"

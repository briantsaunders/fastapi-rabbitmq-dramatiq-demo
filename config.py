import os
from functools import lru_cache

from dotenv import load_dotenv
from pydantic import BaseSettings

load_dotenv()


@lru_cache
def get_app_settings():
    return Settings()


class Settings(BaseSettings):
    PROJECT_NAME: str = "Demo API"
    PROJECT_DESCRIPTION: str = (
        "Demo API to show how you can use RabbitMQ and Dramatiq to run long "
        "running or CPU intensive tasks in the background of a fastapi api."
    )
    RABBITMQ_HOST: str = "rabbitmq"
    RABBITMQ_USER: str = "guest"
    RABBITMQ_PASSWORD: str = "guest"
    RABBITMQ_VHOST: str = "demo"

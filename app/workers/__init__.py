import dramatiq
from dramatiq.brokers.rabbitmq import RabbitmqBroker

from config import get_app_settings

SETTINGS = get_app_settings()


def get_url():
    return (
        f"amqp://{SETTINGS.RABBITMQ_USER}:"
        f"{SETTINGS.RABBITMQ_PASSWORD}"
        f"@{SETTINGS.RABBITMQ_HOST}/{SETTINGS.RABBITMQ_VHOST}"
    )


rabbitmq_broker = RabbitmqBroker(url=get_url())
dramatiq.set_broker(rabbitmq_broker)

from app.workers.task import run_task  # noqa: E402

__all__ = ("run_task",)

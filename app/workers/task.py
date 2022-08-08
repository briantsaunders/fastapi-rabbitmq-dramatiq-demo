import time

from loguru import logger

from app.workers import dramatiq


@dramatiq.actor
def run_task(seconds: int):
    logger.info("task recevied!")
    for x in range(seconds, 0, -1):
        logger.info(f"counting down until task complete - seconds: {x}")
        time.sleep(1)
    logger.info("task completed!")

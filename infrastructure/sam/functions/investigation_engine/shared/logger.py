import json
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)


def log_info(message, **kwargs):
    """
    Log structured information.
    """

    payload = {
        "level": "INFO",
        "message": message
    }

    payload.update(kwargs)

    logger.info(json.dumps(payload))


def log_error(message, **kwargs):
    """
    Log structured errors.
    """

    payload = {
        "level": "ERROR",
        "message": message
    }

    payload.update(kwargs)

    logger.error(json.dumps(payload))
"""Logging utility for calculator operations."""
import logging
import datetime

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
)
logger = logging.getLogger(__name__)


def log_operation(operation, a, b, result):
    """Log a calculator operation with its result."""
    msg = f"{operation}({a}, {b}) = {result}"
    logger.info(msg)
    return msg


def get_timestamp():
    """Return the current timestamp as a string."""
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

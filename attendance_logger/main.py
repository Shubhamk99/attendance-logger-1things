from .api_client import APIClient
from .cron import CRON
from .date_utils import CustomDate
from .holidays import isHolidayToday
from .logger import ResponseLog
from .logging_config import configure_logging, get_logger
from .onething_api import OneThingApi

logger = get_logger("main")


def main():
    configure_logging()

    # Defense in depth for a direct `python3 run.py` - runner.py already
    # checks this before spawning run.py at all.
    if isHolidayToday():
        logger.info("Skipping today's cron run.")
        return

    client = APIClient()

    # Initialize OneThing
    customDate = CustomDate()
    responseLogOneThingApi = ResponseLog("OneThingApi")
    oneThingApi = OneThingApi(client, customDate, responseLogOneThingApi)

    # Cron
    responseLogCRON = ResponseLog("CRON")
    cron = CRON(oneThingApi, responseLogCRON)
    cron.main()

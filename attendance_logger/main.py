from .api_client import APIClient
from .cron import CRON
from .date_utils import CustomDate
from .logger import ResponseLog
from .logging_config import configure_logging
from .onething_api import OneThingApi


def main():
    configure_logging()
    client = APIClient()

    # Initialize OneThing
    customDate = CustomDate()
    responseLogOneThingApi = ResponseLog("OneThingApi")
    oneThingApi = OneThingApi(client, customDate, responseLogOneThingApi)

    # Cron
    responseLogCRON = ResponseLog("CRON")
    cron = CRON(oneThingApi, responseLogCRON)
    cron.main()

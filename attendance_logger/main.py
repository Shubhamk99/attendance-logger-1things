import os
import sys

from .api_client import APIClient
from .cron import CRON
from .date_utils import CustomDate
from .holidays import isHolidayToday
from .logger import ResponseLog
from .logging_config import configure_logging, get_logger
from .onething_api import OneThingApi

logger = get_logger("main")

_CONNECTO_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "connecto-auth-probe")


def _connectoStep(action):
    """Runs the automated Connecto sign-in/sign-out step (see
    connecto_auto.py). Connecto is additive to the existing 1thing.in flow
    below - any failure here (missing session, no photo, network error) is
    logged and swallowed so it never blocks or aborts the day's real
    attendance run."""
    if _CONNECTO_DIR not in sys.path:
        sys.path.insert(0, _CONNECTO_DIR)

    try:
        import connecto_auto
        getattr(connecto_auto, action)()
    except Exception:
        logger.exception("Connecto %s step failed unexpectedly - continuing with the existing attendance flow regardless.", action)


def main():
    configure_logging()

    # Defense in depth for a direct `python3 run.py` - runner.py already
    # checks this before spawning run.py at all.
    if isHolidayToday():
        logger.info("Skipping today's cron run.")
        return

    _connectoStep("signin")

    client = APIClient()

    # Initialize OneThing
    customDate = CustomDate()
    responseLogOneThingApi = ResponseLog("OneThingApi")
    oneThingApi = OneThingApi(client, customDate, responseLogOneThingApi)

    # Cron
    responseLogCRON = ResponseLog("CRON")
    cron = CRON(oneThingApi, responseLogCRON)
    cron.main()

    # Connecto sign-out is temporarily disabled in the daily flow (still
    # implemented in connecto_auto.py - just not called from here yet).
    # _connectoStep("signout")

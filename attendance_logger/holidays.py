import os
from datetime import date

from .logging_config import get_logger, get_project_root

logger = get_logger("holidays")

HOLIDAYS_FILE = os.path.join(get_project_root(), "holidays.txt")


def isHolidayToday():
    if not os.path.exists(HOLIDAYS_FILE):
        return False

    today = date.today().strftime("%Y-%m-%d")
    with open(HOLIDAYS_FILE, "r", encoding="utf-8") as f:
        for line in f:
            entry = line.split("#", 1)[0].strip()
            if entry == today:
                logger.info("Today (%s) is marked as a holiday in %s.", today, HOLIDAYS_FILE)
                return True
    return False

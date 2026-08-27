import calendar
from datetime import datetime


class CustomDate:
    def __init__(self):
        self.today = datetime.now()
        self.attendanceDate = datetime.now().strftime("%Y-%m-%d")
        self.setStartAndEndOfMonth()

    def setStartAndEndOfMonth(self):
        # Start of month
        start_date = self.today.replace(day=1)

        # End of month
        last_day = calendar.monthrange(self.today.year, self.today.month)[1]
        end_date = self.today.replace(day=last_day)

        # Format: M/D/YYYY (no leading zeros)
        self.monthStart = f"{start_date.month}/{start_date.day}/{start_date.year}"
        self.monthEnd = f"{end_date.month}/{end_date.day}/{end_date.year}"

    def currentTimeHHMM(self):
        return datetime.now().strftime("%H:%M")

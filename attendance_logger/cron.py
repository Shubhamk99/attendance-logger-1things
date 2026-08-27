import time
from datetime import datetime, timedelta

from .git_sync import commitAndPushTodayLogs
from .logging_config import get_logger

logger = get_logger("cron")

REQUIRED_DAILY_HOURS = 9


class CRON:
    def __init__(self, oneThingApi, responseLog):
        self.oneThingApi = oneThingApi
        self.responseLog = responseLog

    def getstartTime(self, lastLogoutTimeStr):
        lastLogoutTime = datetime.strptime(lastLogoutTimeStr, "%Y-%m-%d %H:%M:%S")
        now = datetime.now()

        startTime = max(now, lastLogoutTime)

        logger.info("Now: %s", now)
        logger.info("Last logout: %s", lastLogoutTime)
        logger.info("Start time: %s", startTime)

        return self.responseLog.response(startTime, f"Next login time {startTime}")

    def waitTime(self, logType='taskLog'):
        timeLog = self.oneThingApi.getTimeLog()
        logObject = {
            'taskLog': "Time remaining for the next run",
            'signingOff': "Time remaining for the signing off"
        }
        lastLoggedTime = self.oneThingApi.getLastLogOutTime(timeLog)
        startTime = self.getstartTime(lastLoggedTime)

        now = datetime.now()
        startTime += timedelta(seconds=10)
        logger.info("Next login time after adding 10 seconds: %s", startTime)
        while (startTime - now).total_seconds() > 0:
            now = datetime.now()
            timeDiff = self.oneThingApi.calculateTimeDiff(startTime, now)
            logger.info("%s: %s", logObject[logType], timeDiff)
            time.sleep(10)

    def logStatus(self):
        # getTimeLog only reflects blocks that already have an active/actual
        # time log; getTodayTasks also includes UI-scheduled blocks that
        # haven't been logged yet - show both so nothing is hidden.
        self.oneThingApi.getTimeLog(True)
        self.oneThingApi.getTodayTasks(True)

    def isLoggingNeed(self):
        totalHours = self.oneThingApi.getTotalTaskHours()
        data = totalHours < REQUIRED_DAILY_HOURS
        return self.responseLog.response(data, f"Logging needed {data} (total hours: {totalHours})")

    def sendSingingInfo(self):
        self.oneThingApi.sendSignIn()
        self.oneThingApi.sendSignOut()
        commitAndPushTodayLogs()
        return self.responseLog.response(None, "Signin and signout mail.")

    def cronCycle(self):
        if self.isLoggingNeed():
            self.oneThingApi.createTimeLog()
            self.logStatus()

        # To check if after adding the logs we have reached the total logs required.
        if not self.isLoggingNeed():

            # Wait till last tasks logout time
            self.waitTime('signingOff')

            # Send signing info
            self.sendSingingInfo()

        return self.responseLog.response(True, "Cron cycle.")

    def main(self):
        self.oneThingApi.logIn()
        self.logStatus()

        if not self.isLoggingNeed():
            logger.info('All the tasks are logged, will send the signing info after waiting for the current task to end.')
            self.cronCycle()
            return self.responseLog.response(True, "Today's Job Done.")

        logger.info('Logging is needed. Will start the cron after the current task ends.')
        while (self.isLoggingNeed()):
            self.waitTime()
            self.cronCycle()

        return self.responseLog.response(True, "Today's Job Done.")

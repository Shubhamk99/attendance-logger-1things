import json
import time
from datetime import date, datetime

from .logging_config import get_logger

logger = get_logger("onething_api")


class OneThingApi:
    def __init__(self, apiClient, customDate, responseLog):
        self.apiClient = apiClient
        self.customDate = customDate
        self.responseLog = responseLog
        with open("token.json", "r", encoding="utf-8") as f:
            self.token = json.load(f)['token']

    def _postWithRetry(self, endpoint, headers=None, json=None, retries=3, backoff=5):
        # apiClient.post() returns {"error": ...} (no "data" key) on HTTP
        # errors, timeouts, or network exceptions instead of raising - this
        # retries those transient failures instead of letting every caller's
        # response['data'] access crash with an unhandled KeyError.
        response = None
        for attempt in range(1, retries + 1):
            response = self.apiClient.post(endpoint=endpoint, headers=headers, json=json)
            if 'error' not in response:
                return response
            logger.warning("Request to %s failed (attempt %s/%s): %s", endpoint, attempt, retries, response)
            if attempt < retries:
                time.sleep(backoff)
        raise RuntimeError(f"Request to {endpoint} failed after {retries} attempts: {response}")

    def _authedPost(self, endpoint, json=None):
        return self._postWithRetry(endpoint, headers={"Authorization": self.token}, json=json)

    def getLastLogOutTime(self, obj):
        if obj['timelog'] == None:
            resData = datetime.strftime(datetime.now(), "%Y-%m-%d %H:%M:%S")
        else:
            resData = obj['timelog']['end_date_time']

        return self.responseLog.response(resData, f"Last log out time or current time: {resData}")

    def calculateTimeDiff(self, final, initial):
        # Calculate difference
        diff = final - initial

        # Handle past time
        if diff.total_seconds() <= 0:
            return "00:00:00"

        # Convert to hours, minutes, seconds
        total_seconds = int(diff.total_seconds())
        hours, remainder = divmod(total_seconds, 3600)
        minutes, seconds = divmod(remainder, 60)

        return f"{hours:02d}:{minutes:02d}:{seconds:02d}"

    def calculateIdleTime(self):
        # Getting last logged time
        timeLog = self.getTimeLog()
        lastLoggedTime = self.getLastLogOutTime(timeLog)

        # Parse the end_time string
        endTime = datetime.strptime(lastLoggedTime, "%Y-%m-%d %H:%M:%S")

        # Get current time
        now = datetime.now()

        return self.calculateTimeDiff(now, endTime)

    def isTokenValid(self, count=1):
        response = self._authedPost("/checkconnectosignin")

        logger.info("Token check: %s", response)
        if 'error' in response:
            if count < 5:
                time.sleep(30)
                return self.isTokenValid(count + 1)
            return self.responseLog.response(False, "Token invalid tried 4 times.")
        else:
            return self.responseLog.response(True, "Token valid")

    def createTimeLog(self, count=1):
        self.stopTimeLog()
        idleTime = self.calculateIdleTime()
        json = {
            "attendance_date": self.customDate.attendanceDate,
            "selectedTasks": [
                {
                    "task_id": "943172",
                    "task_title": "Development",
                    "workplace_id": "3318",
                    "workplace_name": "PKG - Alpha Data Recruitment",
                    "scheduler_id": int(time.time() * 1000),
                }
            ],
            "taskname": "",
            "selectedList": "",
            "idletime": idleTime,
            "taskscheduler": "",
            "workplace_id": "3318"
        }

        response = self._authedPost("/createTimeLog", json=json)

        if response['data']['status'] == False:
            if count < 5:
                logger.warning("Create time log failed and will wait for 70 sec: %s %s", response['data'], json)
                time.sleep(70)
                return self.createTimeLog(count + 1)
            raise RuntimeError(f"createTimeLog failed after {count} attempts: {response['data']}")

        return self.responseLog.response(response, "Created time log")

    def stopTimeLog(self):
        data = self.getTimeLog()['timelog']
        if data == None:
            return

        json = {
            "attendance_date": self.customDate.attendanceDate,
            "time_log_id": data["id"],
            "startdate_time": data["start_date_time"],
            "enddate_time": data["end_date_time"],
            "autostop": 1
        }

        response = self._authedPost("/stopTimeBlock", json=json)

        if response['data']['status'] == False:
            logger.warning("Stop time log failed: %s %s", response['data'], json)

        return self.responseLog.response(response, "Stopped time log")

    def logIn(self):
        data = None
        if not self.isTokenValid():
            logger.info('Logging in')
            res = self._postWithRetry(
                "/login",
                json={
                    "email": "shubham.k@neosoftmail.com",
                    "password": "768468"
                }
            )
            if res['data']['status'] == True:
                data = res["data"]
                data['attendanceDate'] = self.customDate.attendanceDate
                with open("token.json", "w", encoding="utf-8") as f:
                    json.dump(data, f, indent=4)

            self.token = data['token']

        return self.responseLog.response(self.token, f"Login funtion, token: {self.token}")

    def getTimeLog(self, displayTimeLog=False):
        response = self._authedPost(
            "/lasttimelog",
            json={
                "attendance_date": date.today().strftime("%Y-%m-%d"),
                "workplace_id": "3318"
            }
        )

        log = response['data'] if displayTimeLog else ''
        return self.responseLog.response(response['data'], f"Get time log data. {log}")

    def getSignInMailIds(self):
        response = self._authedPost(
            "/getsigninmailids",
            json={
                "workplace_id": "3318"
            }
        )

        mailData = response['data']['maildata']

        responseData = {
            key: [{"email": email} for email in value]
            for key, value in mailData.items()
        }
        return self.responseLog.response(responseData, "Get signin mailIds")

    def getInTime(self):

        data = self.getTimeLog()['todaylogs']
        times = []

        for key in data.keys():
            start_time_str = key.split(" - ")[0]
            time_obj = datetime.strptime(start_time_str, "%I:%M %p")
            times.append(time_obj)

        earliest = min(times)
        response = earliest.strftime("%H:%M")

        return self.responseLog.response(response, f"Get today's in time: {response}")

    def sendSignIn(self):
        self.sendSignInInfo()
        jsonData = self.getSignInMailIds() | {
            "signininfo": {
                "in_time": self.getInTime(),
                "subject": f"Online for {datetime.now().strftime('%d %B %Y')}",
                "body": "",
                "signature": "Shubham Kashyap",
                "mail_sent": "0"
            },
            "attendance_date": self.customDate.attendanceDate,
            "workplace_id": "3318"
        }

        response = self._authedPost("/sendSignInMail", json=jsonData)

        return self.responseLog.response(response, "Sent today's signin mail.")

    def getTodayTasks(self, displayTasks=False):
        response = self._authedPost(
            "/gettodayTasks",
            json={
                "attendance_date": self.customDate.attendanceDate,
                "workplace_id": "3318"
            }
        )

        taskData = response['data']['taskdata']
        log = taskData if displayTasks else ''
        return self.responseLog.response(taskData, f"Get all today's task. {log}")

    def getTotalTaskHours(self):
        # Covers both UI-scheduled blocks (time_log_id is null) and blocks
        # our own automation created (time_log_id is set) - getTodayTasks
        # returns both kinds.
        taskData = self.getTodayTasks()

        intervals = sorted(
            (
                datetime.strptime(task['start_date'], "%Y-%m-%d %H:%M:%S"),
                datetime.strptime(task['end_date'], "%Y-%m-%d %H:%M:%S"),
            )
            for task in taskData
        )

        # Merge overlapping/adjacent blocks before summing, so overlapping
        # duplicate blocks (e.g. two runner.py instances racing) don't count
        # the same wall-clock time twice. Back-to-back scheduled blocks are
        # adjacent, not overlapping, so this still sums to the same total as
        # a plain sum in the normal case.
        merged = []
        for start, end in intervals:
            if merged and start <= merged[-1][1]:
                merged[-1] = (merged[-1][0], max(merged[-1][1], end))
            else:
                merged.append((start, end))

        total_seconds = sum((end - start).total_seconds() for start, end in merged)
        hours = total_seconds / 3600
        return self.responseLog.response(hours, f"Total scheduled task hours today: {hours}")

    def todayStartTime(self):
        taskData = self.getTodayTasks()
        times = [task['start_date'] for task in taskData]

        dt_times = [datetime.strptime(t, "%Y-%m-%d %H:%M:%S") for t in times]
        earliest = min(dt_times)
        result = earliest.strftime("%H:%M")
        return result

    def sendSignInInfo(self):

        json = {
            "in_time": self.todayStartTime(),
            "subject": f"Online for {datetime.now().strftime('%d %B %Y')}",
            "body": "",
            "signature": "Shubham Kashyap",
            "workplace_id": "3318",
            "attendance_date": self.customDate.attendanceDate,
        }

        response = self._authedPost("/submitsignIn", json=json)

        logger.info("Signin Info: %s %s", response, json)
        return self.responseLog.response(response, "Mark today's sign in.")

    def sendSignOutInfo(self):

        json = {
            "out_time": self.customDate.currentTimeHHMM(),
            "subject": f"Offline for {datetime.now().strftime('%d %B %Y')}",
            "body": "",
            "signature": "Shubham Kashyap",
            "workplace_id": "3318",
            "attendance_date": self.customDate.attendanceDate,
        }

        response = self._authedPost("/submitsignOut", json=json)

        return self.responseLog.response(response, "Mark today's sign out.")

    def getAttendanceData(self):

        response = self._authedPost(
            "/attendance_data",
            json={
                "attendance_date": self.customDate.attendanceDate,
                "end_date": self.customDate.monthEnd,
                "start_date": self.customDate.monthStart,
                "workplace_id": "3318",
            }
        )

        responseData = {
            "signininfo": response['data']["sigininfo"],
            "signoutinfo": response['data']["signoutinfo"]
        }
        return self.responseLog.response(responseData, "Get today's signIn and signOut info.")

    def sendSignOut(self):
        self.sendSignOutInfo()
        json = self.getSignInMailIds() | self.getAttendanceData() | {
            "attendance_date": self.customDate.attendanceDate,
            "taskarray": self.getTodayTasks(),
            "workplace_id": "3318"
        }
        response = self._authedPost("/sendSignOutMail", json=json)

        return self.responseLog.response(response, "Send sign out mail.")

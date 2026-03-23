import requests
import certifi
from typing import Dict, Any, Optional
import time
import json
import schedule
from datetime import date, datetime, timedelta
import calendar

import warnings
from urllib3.exceptions import InsecureRequestWarning
warnings.simplefilter("ignore", InsecureRequestWarning)

class ResponseLog:
    def __init__(self, className = None):
        self.className = className

    def response(self, data, log=""):
        print(self.className+": "+log)
        return data

class CustomeDate:
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

class APIClient:
    def __init__(self, default_headers: Optional[Dict[str, str]] = None):
        """
        Initialize API client with base URL and optional default headers.
        """
        self.base_url = "https://be.1-thing.in" #base_url.rstrip("/")
        self.default_headers = default_headers or {
            "Content-Type": "application/json",
            "Accept": "application/json",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 Safari/537.36",
            "Referer": "https://1-thing.in/",
            "origin": "https://1-thing.in"
        }
        self.token = None

    def _build_url(self, endpoint: str) -> str:
        """
        Construct full URL.
        """
        return f"{self.base_url}/{endpoint.lstrip('/')}"


    def _parse_response(self, response: requests.Response) -> Any:
        """
        Safely parse response JSON or return text.
        """
        try:
            return response.json()
        except ValueError:
            return response.text

    def post(
        self,
        endpoint: str,
        data: Optional[Dict[str, Any]] = None,
        json: Optional[Dict[str, Any]] = None,
        headers: Optional[Dict[str, str]] = None,
        params: Optional[Dict[str, Any]] = None,
        files: Optional[Dict[str, Any]] = None,
        timeout: int = 30,
    ) -> Dict[str, Any]:
        """
        Make a POST request.
        """
        url = self._build_url(endpoint)
        request_headers = {**self.default_headers, **(headers or {})}

        try:
            response = requests.post(
                url=url,
                data=data,
                json=json,
                headers=request_headers,
                params=params,
                timeout=timeout,
                files=files,
                verify = False,
                # verify=certifi.where(),
            )

            response.raise_for_status()

            return {
                "headers": response.headers,
                "status_code": response.status_code,
                "data": self._parse_response(response),
            }

        except requests.exceptions.HTTPError as http_err:
            return {"error": "HTTP error", "details": str(http_err)}

        except requests.exceptions.Timeout:
            return {"error": "Request timed out"}

        except requests.exceptions.RequestException as err:
            return {"error": "Request failed", "details": str(err)}

class OneThingApi():
    def __init__(self, apiClient, customDate, responseLog):
        self.apiClient = apiClient
        self.customDate = customDate
        self.responseLog = responseLog
        with open("token.json", "r", encoding="utf-8") as f:
            self.token = json.load(f)['token']

    def getLastLogOutTime(self, obj):
        resData = None
        if obj['timelog'] == None:
            resData = datetime.strftime(datetime.now(), "%Y-%m-%d %H:%M:%S")
            # return self.responseLog.response(resData)
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
        
    def isTokenValid(self, count = 1):
        response = self.apiClient.post(
            headers={
                "Authorization": self.token,
            },
            endpoint="/checkconnectosignin",
        )

        print("Token check: ", response)
        if 'error' in response:
            if (count<5):
                time.sleep(30)
                self.isTokenValid(count+1)
            return self.responseLog.response(False, f"Token invalid tried 4 times.")
        else:
            return self.responseLog.response(True, "Token valid")
        
    def createTimeLog(self, count = 1):
        idleTime = self.calculateIdleTime()
        json = {
            "attendance_date": self.customDate.attendanceDate,
            "selectedTasks":[
                {
                    "task_id":"940641",
                    "task_title":"Onboarding",
                    "workplace_id":"3318",
                    "workplace_name":"PKG - Alpha Data Recruitment",
                    "scheduler_id": int(time.time() * 1000),
                }
            ],
            "taskname":"",
            "selectedList":"",
            "idletime": idleTime,
            "taskscheduler":"",
            "workplace_id":"3318"
        }

        response = self.apiClient.post(
            headers={
                "Authorization": self.token,
            },
            endpoint="/createTimeLog",
            json=json
        )

        if (response['data']['status'] == False and count<5):
            print("Create time log failed and will wait for 70 sec: ", response['data'], json)
            time.sleep(70)
            self.createTimeLog(count+1)
        elif (response['data']['status'] == False and count<=5):
            return ValueError

        return self.responseLog.response(response, "Created time log")
    
    def logIn(self):
        data = None
        if not self.isTokenValid(): 
            print('Logging in')
            res = self.apiClient.post(
                endpoint="/login",
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

    def getTimeLog(self):
        response = self.apiClient.post(
            headers={
                "Authorization": self.token,
            },
            endpoint="/lasttimelog",
            json= {
                "attendance_date":date.today().strftime("%Y-%m-%d"),
                "workplace_id":"3318"
            }
        )

        return self.responseLog.response(response['data'], "Get time log data.")
    
    def getSignInMailIds(self):
        response = self.apiClient.post(
            headers={
                "Authorization": self.token,
            },
            endpoint="/getsigninmailids",
            json={
                "workplace_id":"3318"
            }
        )
        
        mailData =  response['data']['maildata']
    
        responseData = {
            key: [{"email": email} for email in value]
            for key, value in mailData.items()
        }
        return self.responseLog.response(responseData, "Get signin mailIds")

    def getInTime(self):
        # jsonData = {
        #     "attendance_date": self.customDate.attendanceDate,
        #     "end_date": self.customDate.monthEnd,
        #     "start_date": self.customDate.monthStart,
        #     "workplace_id":"3318",
        # }

        # response = self.apiClient.post(
        #     headers={
        #         "Authorization": self.token,
        #     },
        #     endpoint="/attendance_data",
        #     json=jsonData
        # )

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
        jsonData =  self.getSignInMailIds() | {
            "signininfo":{
                "in_time": self.getInTime(),
                "subject":f"Online for {datetime.now().strftime('%d %B %Y')}",
                "body":"",
                "signature":"Shubham Kashyap",
                "mail_sent":"0"
            },
            "attendance_date": self.customDate.attendanceDate,
            "workplace_id":"3318"
        }

        response = self.apiClient.post(
            headers={
                "Authorization": self.token,
            },
            endpoint="/sendSignInMail",
            json=jsonData
        )

        return self.responseLog.response(response, "Sent today's signin mail.")

    def getTodayTasks(self):
        response = self.apiClient.post(
            headers={
                "Authorization": self.token,
            },
            endpoint="/gettodayTasks",
            json = {
                "attendance_date": self.customDate.attendanceDate,
                "workplace_id": "3318"
            }
        )

        return self.responseLog.response(response['data']['taskdata'], "Get all today's task.")

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

        response = self.apiClient.post(
            headers={
                "Authorization": self.token,
            },
            endpoint="/submitsignIn",
            json = json
        )

        print("Signin Info: ", response, json)
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

        response = self.apiClient.post(
            headers={
                "Authorization": self.token,
            },
            endpoint="/submitsignOut",
            json = json
        )

        return self.responseLog.response(response, "Mark today's sign out.")

    def getAttendanceData(self):
        
        response = self.apiClient.post(
            headers={
                "Authorization": self.token,
            },
            endpoint="/attendance_data",
            json = {
                "attendance_date": self.customDate.attendanceDate,
                "end_date": self.customDate.monthEnd,
                "start_date": self.customDate.monthStart,
                "workplace_id":"3318",
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
            "attendance_date":self.customDate.attendanceDate,
            "taskarray": self.getTodayTasks(),
            "workplace_id":"3318"
        }
        response = self.apiClient.post(
            headers={
                "Authorization": self.token,
            },
            endpoint="/sendSignOutMail",
            json = json
        )

        return self.responseLog.response(response, "Send sign out mail.")

class CRON:
    def __init__(self, oneThingApi, responseLog):
        self.oneThingApi = oneThingApi
        self.responseLog = responseLog

    def getstartTime(self, lastLogoutTimeStr):
        lastLogoutTime = datetime.strptime(lastLogoutTimeStr, "%Y-%m-%d %H:%M:%S")
        now = datetime.now()
        
        start_time = max(now, lastLogoutTime)
        
        print("Now:", now)
        print("Last logout:", lastLogoutTime)
        print("Start time:", start_time)
        
        return self.responseLog.response(start_time, f"Next login time on starting the program {start_time}")

    def waitTime(self, timeLog):
        lastLoggedTime = self.oneThingApi.getLastLogOutTime(timeLog)
        startTime = self.getstartTime(lastLoggedTime)

        now = datetime.now()
        startTime += timedelta(seconds=0)
        while (startTime - now).total_seconds() > 0:
            now = datetime.now()
            timeDiff = self.oneThingApi.calculateTimeDiff(startTime, now)
            print(f"Time remaining for first run log: {timeDiff}" )
            time.sleep(10)

    def isWaitTimeMoreThan175mins(self):
        timeLog = self.oneThingApi.getTimeLog()
        lastLoggedTime = self.oneThingApi.getLastLogOutTime(timeLog)
        lastLoggedTime = datetime.strptime(lastLoggedTime, "%Y-%m-%d %H:%M:%S")

        now = datetime.now()
        return (now - lastLoggedTime).total_seconds() > 4500

    def isLoggingNeed(self, obj):
        data = len(obj['timelogidarray']) != 9
        return self.responseLog.response(data, f"Logging needed {data}")

    def sendSingingInfo(self):
        self.oneThingApi.sendSignIn()
        self.oneThingApi.sendSignOut()
        return self.responseLog.response(None, "Signin and signout mail.")

    def cronCycle(self):
        timeLog = self.oneThingApi.getTimeLog()
        if self.isLoggingNeed(timeLog):
            self.oneThingApi.createTimeLog()
        
        # To check if after adding the logs we have reached the total logs required.
        timeLog = self.oneThingApi.getTimeLog()
        if not self.isLoggingNeed(timeLog): 

            # Wait till last tasks logout time
            self.waitTime(timeLog)

            # Send signing info
            self.sendSingingInfo()
            return self.responseLog.response(schedule.CancelJob, "Cron cycle, END.")
        
        self.nextCronTime = datetime.now() + timedelta(hours=1, seconds=1) #Isec buffer for proper esitmationi calculation
        return self.responseLog.response(True, "Cron cycle.")
        
    def main(self):
        self.oneThingApi.logIn()
        timeLog = self.oneThingApi.getTimeLog()
        if self.isLoggingNeed(timeLog):
            self.waitTime(timeLog)
            res = self.cronCycle()
            # If already the last call don't do anything
            if res == True:
                schedule.every(61).minutes.do(self.cronCycle)

                self.nextCronTime = datetime.now() + timedelta(hours=1, minutes=1)
                while len(schedule.jobs):
                    schedule.run_pending()
                    time.sleep(10)
                    timeDiff = self.oneThingApi.calculateTimeDiff(self.nextCronTime, datetime.now())
                    print(f"Time remaining for next cron: {timeDiff}" )

        # In case attendace is logged but not signing info
        else:
            self.cronCycle()

        return self.responseLog.response(True, "Today's Job Done.")

def main():
    client = APIClient()

    # Initialize OneThing
    customeDate = CustomeDate()
    responseLogOneThingApi = ResponseLog("OneThingApi")
    oneThingApi = OneThingApi(client, customeDate, responseLogOneThingApi)

    # Cron
    responseLogCRON = ResponseLog("CRON")
    cron = CRON(oneThingApi, responseLogCRON)
    cron.main()

def second():
    client = APIClient()

    # Initialize OneThing
    customeDate = CustomeDate()
    responseLogOneThingApi = ResponseLog("OneThingApi")
    oneThingApi = OneThingApi(client, customeDate, responseLogOneThingApi)

    # Cron
    responseLogCRON = ResponseLog("CRON")
    cron = CRON(oneThingApi, responseLogCRON)
    print(cron.isWaitTimeMoreThan175mins())

main()
# second()
import requests
from datetime import date, datetime, timedelta
import certifi

import warnings
from urllib3.exceptions import InsecureRequestWarning
warnings.simplefilter("ignore", InsecureRequestWarning)

# headers = {
#     "Content-Type": "application/json",
#     "Accept": "application/json, text/plain, */*",

#     # Browser identity headers
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 Safari/537.36",
#     "Referer": "https://1-thing.in/",
#     "Origin": "https://1-thing.in",

#     # Chrome client hints
#     "sec-ch-ua": '"Chromium";v="146", "Not-A.Brand";v="24", "Google Chrome";v="146"',
#     "sec-ch-ua-platform": '"Windows"',
#     "sec-ch-ua-mobile": "?0",

#     "Authorization": "eyJpdiI6IjNrUE1OZG1Ka3FJQkVtOURES0d1Nnc9PSIsInZhbHVlIjoibnIwNkhJempoQzBKXC9KaVwvekxxOGd1cEFtOWxCTjI0Z01tQTliN0ZXc1JvPSIsIm1hYyI6ImNjNTFiMzM2MjQwNWYxNWQ4OGYzZWZhNTllOGM0NDBkNDBkMWZmYjg4MDBjZjZmMDkwMjkwNGQ3Mjc2MWFiMjYifQ=="
# }


# def todayStartTimeFinal(self):
#     r = self.apiClient.post(
#         endpoint = "/gettodayTasks",
#         headers={
#             "Authorization": self.token,
#         },
#         json = {
#             "attendance_date": self.customDate.attendanceDate, #update to today's date
#             "workplace_id":"3318",
#         }
#     )

#     response = r.json()
#     times = [task['start_date'] for task in response['taskdata']]

#     dt_times = [datetime.strptime(t, "%Y-%m-%d %H:%M:%S") for t in times]
#     earliest = min(dt_times)
#     result = earliest.strftime("%H:%M")
#     return result


# def todayStartTime():
#     r = requests.post(
#         "https://be.1-thing.in/gettodayTasks",
#         headers=headers,
#         json = {
#             "attendance_date": "2026-03-18", #update to today's date
#             "workplace_id":"3318",
#         },
#         verify = False
#     )

#     response = r.json()
#     times = [task['start_date'] for task in response['taskdata']]

#     dt_times = [datetime.strptime(t, "%Y-%m-%d %H:%M:%S") for t in times]
#     earliest = min(dt_times)
#     result = earliest.strftime("%H:%M")
#     return result

# # print('today start time:', todayStartTime())

# def minTime(times):
#     # Convert to datetime objects
#     dt_times = [datetime.strptime(t, "%Y-%m-%d %H:%M:%S") for t in times]

#     # Get earliest
#     earliest = min(dt_times)

#     result = earliest.strftime("%H:%M")
#     print(result)
#     return(result)

def get_earliest_login_time(data):
    times = []

    for key in data.keys():

        start_time_str = key.split(" - ")[0]  # get "10:37 AM"
        time_obj = datetime.strptime(start_time_str, "%I:%M %p")
        print(time_obj.strftime("%H:%M"))
        times.append(time_obj)

    earliest = min(times)
    return earliest.strftime("%H:%M")

try:
    headers = {
      "Content-Type": "application/json",
      "Accept": "application/json, text/plain, */*",

      # Browser identity headers
      "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 Safari/537.36",
      "Referer": "https://1-thing.in/",
      "Origin": "https://1-thing.in",

      # Chrome client hints
      "sec-ch-ua": '"Chromium";v="146", "Not-A.Brand";v="24", "Google Chrome";v="146"',
      "sec-ch-ua-platform": '"Windows"',
      "sec-ch-ua-mobile": "?0",

      "Authorization": "eyJpdiI6IjNrUE1OZG1Ka3FJQkVtOURES0d1Nnc9PSIsInZhbHVlIjoibnIwNkhJempoQzBKXC9KaVwvekxxOGd1cEFtOWxCTjI0Z01tQTliN0ZXc1JvPSIsIm1hYyI6ImNjNTFiMzM2MjQwNWYxNWQ4OGYzZWZhNTllOGM0NDBkNDBkMWZmYjg4MDBjZjZmMDkwMjkwNGQ3Mjc2MWFiMjYifQ=="
    }

    r = requests.post(
        "https://be.1-thing.in/lasttimelog",
        headers=headers,
        json= {
            "attendance_date":"2026-03-18",
            "workplace_id":"3318"
        },
        verify = False
    )

    response = r.json()['todaylogs']
    print(get_earliest_login_time(response)+"a")

except Exception as e:

    print("ERROR:", e)


# singInData = {"in_time":"10:05","subject":"Online for 18 March 2026","body":"","signature":"","workplace_id":"3318","attendance_date":"2026-03-18"}

import time
print(int(time.time() * 1000))


now = datetime.now()
startTime = now - timedelta(hours=1, minutes=16)
print((now - startTime).total_seconds() > 4500)
# return (now - startTime).total_seconds() > 4500
# "C:\Users\shubh\AppData\Local\Programs\Python\Python310\python.exe" -m pip install certifi
# "C:\Users\shubh\AppData\Local\Programs\Python\Python310\python.exe" -m pip install --upgrade certifi
# "C:\Users\shubh\AppData\Local\Programs\Python\Python310\python.exe" -m certifi
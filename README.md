# attendance-logger-1things

Automates daily attendance logging (time-block creation, sign-in/sign-out mail) against the 1thing.in API.

## Layout

```
attendance_logger/     # package with the actual logic
  api_client.py         # thin HTTP wrapper (APIClient)
  onething_api.py        # 1thing.in API calls (OneThingApi)
  cron.py                 # scheduling loop that drives a day's cycle (CRON)
  date_utils.py            # attendance date / month-range helpers (CustomDate)
  logger.py                 # ResponseLog, thin wrapper around the logging module
  logging_config.py          # configures per-day log files under logs/
  git_sync.py                 # commits + pushes today's log file after sign-off
  main.py                      # wires the above together and runs one cycle
run.py                  # entry point: `python3 run.py`
runner.py               # supervisor that restarts run.py on non-zero exit
scripts/
  dev_debug.py           # scratch script for manual API debugging, not part of the app
token.json              # cached auth token + session state (overwritten on login)
logs/
  YYYY-MM-DD.txt          # one log file per day, written by every entry point and committed/pushed after sign-off
plan.txt                # notes on the cron scheduling logic
requirements.txt
```

## Running

```
python3 run.py       # single run
python3 runner.py    # keeps restarting run.py if it exits non-zero
```

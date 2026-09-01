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

## Running automatically (launchd)

A system-wide **LaunchDaemon** starts `runner.py` on its own every weekday at
9:00 AM, so no terminal or login session needs to be open:

- Plist: `/Library/LaunchDaemons/com.attendance-logger.daily.plist`
  (root-owned, system domain - loaded automatically at boot since it lives in
  `/Library/LaunchDaemons`).
- Runs as system user `comprint` (`UserName`/`HOME` in the plist), **not**
  whichever user is logged in - so `ps aux | grep runner.py` shows `comprint`
  as the owner, and managing the job (kickstart, bootout, print) needs
  `sudo` regardless of who's logged in.
- Schedule: `StartCalendarInterval` for Mon-Fri, 09:00. No `RunAtLoad` (so
  reloading the job doesn't also trigger an immediate run) and no
  `KeepAlive` - if the process is killed or crashes mid-day, it will **not**
  restart itself; the next trigger is the following weekday at 9:00.
- Output: stdout/stderr both go to `launchd.log` in the project root.

Manage it with:
```
sudo launchctl print system/com.attendance-logger.daily        # check status
sudo launchctl kickstart -k system/com.attendance-logger.daily # force an immediate (re)start
sudo launchctl bootout system/com.attendance-logger.daily      # deactivate
sudo launchctl bootstrap system /Library/LaunchDaemons/com.attendance-logger.daily.plist  # activate
```

### Project files must stay owned by `comprint`, not group-writable

launchd runs a security/code-integrity check before starting a system
daemon, and refuses to launch it if the working directory (this whole repo)
isn't owned by the daemon's configured user (`comprint`) or is
group/other-writable - it fails silently from the outside, showing up only
as `state = not running`, `last exit code = 78: EX_CONFIG` in
`launchctl print`. This actually happened during development: recursively
`chown`-ing the repo to a different admin user (to allow editing) broke the
daemon until ownership was reverted with
`sudo chown -R comprint . && sudo chmod -R g-w .`.

So: to edit a file here, either have `comprint` (or `sudo`) make the edit
directly, or narrowly `chown`/`chmod` just the one file, make the edit, then
restore it to `comprint:wheel` with its original mode (644 for files, 755
for dirs) *before* restarting/kickstarting the daemon.

### Single-instance guard

`runner.py` takes an exclusive `flock` on `runner.lock` (project root) at
startup and exits immediately if another instance already holds it. This
guards against launchd double-dispatching the daemon for a single trigger
(observed once in practice, causing two `runner.py`/`run.py` process trees
to run concurrently and create duplicate/overlapping attendance log entries
for the same time block). The lock is OS-held, so it can't go stale even if
a process is killed or crashes.

### Keeping the Mac awake for the whole run

The cron loop can span several hours in a day (waits until 9 total hours are
logged), so the Mac needs to stay up the entire time, not just at 9:00:

- `runner.py` runs `caffeinate -s -i` for its own lifetime. `-s` (prevent
  system sleep) is what actually stops lid-closed sleep, but it **only holds
  while on AC power** - unplugged, it's a no-op and lid-closed sleep will
  interrupt the run.
- A recurring hardware wake is scheduled at the OS level (`pmset -g sched`
  shows `wakepoweron at 8:59AM weekdays only`) so the Mac physically wakes
  itself just before the 9:00 trigger, regardless of lid state. This isn't
  part of the repo - it's a standing `sudo pmset repeat` system setting.
- Net effect: this is reliable if the Mac is plugged in every morning. On
  battery with the lid closed, expect the old symptom - the Mac only gets
  brief ~17-minute maintenance dark-wakes, which is enough to make patchy
  progress but not a continuous run.

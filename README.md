# attendance-logger-1things

Automates daily attendance logging (time-block creation, sign-in/sign-out mail) against the 1thing.in API.

## Layout

```
attendance_logger/     # package with the actual logic
  api_client.py         # thin HTTP wrapper (APIClient)
  onething_api.py        # 1thing.in API calls (OneThingApi)
  cron.py                 # scheduling loop that drives a day's cycle (CRON)
  date_utils.py            # attendance date / month-range helpers (CustomDate)
  holidays.py               # checks today's date against holidays.txt
  logger.py                  # ResponseLog, thin wrapper around the logging module
  logging_config.py           # configures per-day log files under logs/
  git_sync.py                  # commits + pushes today's log file after sign-off
  main.py                       # wires the above together and runs one cycle
run.py                  # entry point: `python3 run.py`
runner.py               # supervisor that restarts run.py on non-zero exit
scripts/
  dev_debug.py           # scratch script for manual API debugging, not part of the app
token.json              # cached auth token + session state (overwritten on login)
holidays.txt             # dates to skip entirely - see "Marking a holiday" below
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

## Marking a holiday

To skip a weekday entirely (a company holiday, leave day, etc.), add its
date to `holidays.txt` in the project root, one `YYYY-MM-DD` line per date
(`#` starts a comment). `runner.py` checks this file first, before doing
anything else - before the single-instance lock, before `caffeinate`, before
spawning `run.py` - so a holiday results in no API calls and no time log for
that day at all. It exits cleanly (exit code 0), so launchd just waits for
the next scheduled weekday same as a normal completed day.

The check also runs a second time inside `attendance_logger/main.py`, so a
direct `python3 run.py` respects `holidays.txt` too, not just the
`runner.py`/launchd path.

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

### The project root directory must stay owned by `comprint`, not group/other-writable

launchd runs a security/code-integrity check before starting a system
daemon, and refuses to launch it if the **project root directory itself**
isn't owned by the daemon's configured user (`comprint`) or is
group/other-writable (classic POSIX mode bits) - it fails silently from the
outside, showing up only as `state = not running`,
`last exit code = 78: EX_CONFIG` in `launchctl print`. This actually
happened during development: recursively `chown`-ing the repo to a
different admin user, and separately `chmod -R g+w`-ing it, both broke the
daemon until reverted with `sudo chown -R comprint . && sudo chmod -R g-w .`.

The check only looks at the root directory's own owner/mode, not each
file's - individual files inside can be owned by someone else without
breaking anything, and a macOS ACL (`chmod +a`, additive, doesn't touch the
classic owner/mode bits the check inspects) can grant another user full
read/write/delete access to the whole tree safely. That's how Shubham has
direct write access here:
```
sudo chmod -R +a "user:Shubham allow read,write,execute,append,delete,delete_child,readattr,writeattr,readextattr,writeextattr,readsecurity,writesecurity,file_inherit,directory_inherit" .
```
`delete_child` matters specifically - without it, Shubham can create new
files but can't overwrite/rename over an existing one (most editors,
including Claude Code's file-edit tool, write a temp file and rename it
over the original). `file_inherit`/`directory_inherit` make new files
created later pick up the same grant automatically. After any ACL change,
verify with `sudo launchctl kickstart -k system/com.attendance-logger.daily`
that the daemon still comes up (`state = running` in `launchctl print`) - if
not, `sudo chmod -R -N .` strips all ACLs back to a clean slate.

If you don't want to touch permissions at all, `sudo -u comprint <command>`
runs anything (edits, git, launchctl) as `comprint` directly, using your own
password for `sudo` rather than `comprint`'s - no ownership/ACL change
needed.

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

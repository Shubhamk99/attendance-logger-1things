import os
import subprocess
from datetime import date

from .logging_config import get_logger, get_project_root, get_today_log_file

logger = get_logger("git_sync")


def _run(args):
    return subprocess.run(
        args,
        cwd=get_project_root(),
        capture_output=True,
        text=True,
    )


def commitAndPushTodayLogs():
    """Commit and push today's log file. Never raises - if git isn't
    available, there's nothing to commit, or the push fails (e.g. an
    expired remote token), just log it and move on."""
    logFile = get_today_log_file()
    relLogFile = os.path.relpath(logFile, get_project_root())

    try:
        add = _run(["git", "add", relLogFile])
        if add.returncode != 0:
            logger.warning("git add failed, leaving logs uncommitted: %s", add.stderr.strip())
            return

        # --only restricts the commit to just this path, even if other
        # files happen to be staged for something else at the time.
        commit = _run(["git", "commit", "--only", "-m", f"Add logs for {date.today().strftime('%Y-%m-%d')}", "--", relLogFile])
        if commit.returncode != 0:
            if "nothing to commit" in commit.stdout.lower():
                logger.info("No new log changes to commit.")
            else:
                logger.warning("git commit failed, leaving logs uncommitted: %s", commit.stdout.strip() or commit.stderr.strip())
            return

        logger.info("Committed today's logs.")

        push = _run(["git", "push"])
        if push.returncode != 0:
            logger.warning("git push failed (e.g. expired token) - commit stays local: %s", push.stderr.strip())
        else:
            logger.info("Pushed today's logs.")

    except FileNotFoundError:
        logger.warning("git executable not found - skipping log commit/push.")

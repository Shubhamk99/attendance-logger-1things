import os
import subprocess
import sys
import time
import platform

from attendance_logger.logging_config import configure_logging, get_logger

configure_logging()
logger = get_logger("runner")

# Path to the Python file you want to run
script_path = "run.py"

# Time to wait between runs (seconds)
interval_seconds = 5
# Reuse the exact interpreter this runner was launched with, so the child
# process always sees the same installed packages regardless of PATH.
PYTHON = sys.executable
logger.info("Using interpreter: %s", PYTHON)

# Keep the Mac awake for as long as this runner is alive. caffeinate exits
# on its own once this process (pid) exits, so there's nothing to clean up.
if platform.system() == "Darwin":
    subprocess.Popen(["caffeinate", "-i", "-w", str(os.getpid())])

try:
    while True:
        logger.info("Starting script: %s", script_path)
        # Run the other script and wait for it to finish
        result = subprocess.Popen(
            [PYTHON, "-u", script_path],
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True
        )

        # Relay the child's own (already timestamped/leveled) log lines as-is.
        for line in result.stdout:
            print(line, end="")

        # Wait for process to finish
        result.wait()

        # Check exit code
        if result.returncode == 0:
            logger.info("Child script exited normally. Stopping runner.")
            break  # exit the loop if child exits normally
        else:
            logger.warning("Child script exited with code %s. Restarting in %s seconds...", result.returncode, interval_seconds)
            time.sleep(interval_seconds)

except KeyboardInterrupt:
    logger.info("Runner stopped manually.")

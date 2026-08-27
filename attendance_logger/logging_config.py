import logging
import os
import sys
from datetime import datetime

_CONFIGURED = False

# Anchored to the project root (parent of this package), so log files
# always resolve to the same place regardless of the process's cwd.
_PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
_LOG_DIR = os.path.join(_PROJECT_ROOT, "logs")


def get_project_root():
    return _PROJECT_ROOT


def get_today_log_file():
    return os.path.join(_LOG_DIR, f"{datetime.now().strftime('%Y-%m-%d')}.txt")


def configure_logging(level=logging.INFO):
    global _CONFIGURED
    if _CONFIGURED:
        return

    os.makedirs(_LOG_DIR, exist_ok=True)
    log_file = get_today_log_file()

    formatter = logging.Formatter(
        "%(asctime)s %(levelname)s %(name)s: %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )

    stream_handler = logging.StreamHandler(sys.stdout)
    stream_handler.setFormatter(formatter)

    file_handler = logging.FileHandler(log_file)
    file_handler.setFormatter(formatter)

    root = logging.getLogger("attendance_logger")
    root.setLevel(level)
    root.addHandler(stream_handler)
    root.addHandler(file_handler)
    root.propagate = False

    _CONFIGURED = True


def get_logger(name):
    return logging.getLogger(f"attendance_logger.{name}")

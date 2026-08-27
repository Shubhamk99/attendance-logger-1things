from .logging_config import get_logger


class ResponseLog:
    def __init__(self, className=None):
        self.className = className
        self._logger = get_logger(className or "ResponseLog")

    def response(self, data, log=""):
        self._logger.info(log)
        return data


import logging
from logging.handlers import RotatingFileHandler
import json, time

LOGFILE = "bot.log"

class JsonFormatter(logging.Formatter):
    def format(self, record):
        data = {
            "ts": time.time(),
            "level": record.levelname,
            "msg": record.getMessage()
        }
        if record.exc_info:
            data["exc_info"] = self.formatException(record.exc_info)
        return json.dumps(data)

def get_logger(name="binance_bot"):
    logger = logging.getLogger(name)
    if logger.handlers:
        return logger
    handler = RotatingFileHandler(LOGFILE, maxBytes=5_000_000, backupCount=3)
    handler.setFormatter(JsonFormatter())
    logger.setLevel(logging.INFO)
    logger.addHandler(handler)
    console = logging.StreamHandler()
    console.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(message)s"))
    logger.addHandler(console)
    return logger

logger = get_logger()

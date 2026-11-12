import os
from datetime import datetime
import logging
import structlog


class CustomLogger:
    # attributes
    # methods
    # constructor
    def __init__(self):
        # 1. create the folder
        self.LOG_FOLDER = os.path.join(os.getcwd(), "logs")
        os.makedirs(self.LOG_FOLDER, exist_ok=True)
        # 2.create filename path
        # 11_10_2016.log
        LOG_FILE_NAME = f"{datetime.now().strftime('%m_%d_%Y')}.log"
        self.LOG_FILE_PATH = os.path.join(self.LOG_FOLDER, LOG_FILE_NAME)
        # 'c:\\Users\\Admin\\OneDrive\\Desktop\\Knowledge_Assist_10AM\\beckend\\logger\\logs\\11_05_2026.log'

    def get_logger(self, name=__file__):
        logger_name = os.path.basename(name)

        # for file handler
        file_handler = logging.FileHandler(self.LOG_FILE_PATH)
        file_handler.setLevel(logging.INFO)
        file_handler.setFormatter(logging.Formatter(
            "%(message)s"))

        # for console handler
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.INFO)
        console_handler.setFormatter(logging.Formatter("%(message)s"))

        logging.basicConfig(
            level=logging.INFO,
            format="%(message)s",
            handlers=[file_handler, console_handler]
        )

        # configure structlog for JSON structired logging
        structlog.configure(
            processors=[
                structlog.processors.TimeStamper(
                    fmt="iso", utc=True, key="timestamp"),
                structlog.processors.add_log_level,
                structlog.processors.EventRenamer(to="event"),
                structlog.processors.JSONRenderer()
            ],
            logger_factory=structlog.stdlib.LoggerFactory(),
            cache_logger_on_first_use=True,
        )

        return structlog.get_logger(logger_name)


# loggerobj = CustomLogger()
# logger = loggerobj.get_logger()
# logger.info("i am callong from custom logger")

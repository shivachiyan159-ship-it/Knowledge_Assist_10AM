from .custom_logger import CustomLogger

loggerobj = CustomLogger()
GLOBAL_LOGGER = loggerobj.get_logger("knowledge_assist_10am")

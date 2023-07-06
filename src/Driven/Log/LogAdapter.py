from src.Port.LogPort import LogPort
from sys import stdout
import logging

class LogAdapter(LogPort):
    def __init__(self) -> None:
        self.__logger = logging.getLogger('quotation_logger')
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        handler = logging.StreamHandler(stream=stdout)
        handler.setFormatter(fmt=formatter)
        self.__logger.setLevel(level=logging.INFO)
        self.__logger.addHandler(hdlr=handler)

    def info(self, message: str) -> None:
        self.__logger.info(msg=message)

    def error(self, message: str) -> None:
        self.__logger.error(msg=message)

    def critical(self, message: str) -> None:
        self.__logger.critical(msg=message)
    
    def warning(self, message: str) -> None:
        self.__logger.warning(msg=message)
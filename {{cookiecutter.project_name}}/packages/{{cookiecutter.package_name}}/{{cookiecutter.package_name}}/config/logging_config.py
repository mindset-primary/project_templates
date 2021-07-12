import logging
import sys
from types import FrameType
from typing import List, cast

from loguru import logger
from pydantic import AnyHttpUrl, BaseSettings

### LOGGING DATA PROCESSING/ANALYSIS ###

class ProcessLogger:
    def __init__(self, module):
        self.module = module
        self.processLogger = logging.getLogger(self.module)
        self.processLogger.setLevel(logging.INFO)
        formatter = logging.Formatter('%(asctime)s:%(name)s:%(message)s')
        file_handler = logging.FileHandler('logs/process_log.log')
        file_handler.setFormatter(formatter)
        self.processLogger.addHandler(file_handler)

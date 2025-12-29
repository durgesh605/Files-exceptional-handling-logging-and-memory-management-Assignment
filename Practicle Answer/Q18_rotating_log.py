"""
Q18. How would you implement a basic logging setup that logs to a file with rotation after 1MB?
"""
import logging
from logging.handlers import RotatingFileHandler
handler=RotatingFileHandler("rotate.log",maxBytes=1000000,backupCount=1)
logging.basicConfig(handlers=[handler],level=logging.INFO)
logging.info("Rotating log")

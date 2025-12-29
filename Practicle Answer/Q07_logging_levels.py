"""
Q7. How do you log information at different levels (INFO, WARNING, ERROR) using logging module?
"""
import logging
logging.basicConfig(level=logging.INFO)
logging.info("Info message")
logging.warning("Warning message")
logging.error("Error message")

"""
Q14. Write a program that uses the logging module to log both informational and error messages.
"""
import logging
logging.basicConfig(filename="app.log",level=logging.INFO)
logging.info("Program started")
logging.error("Error occurred")
print("Logs written")

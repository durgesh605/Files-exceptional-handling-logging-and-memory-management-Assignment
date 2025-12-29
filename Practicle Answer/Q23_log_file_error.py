"""
Q23. Write a Python program that writes an error message to a log file when an error occurs during file handling.
"""
import logging
logging.basicConfig(filename="file_error.log",level=logging.ERROR)
try:
    open("nofile.txt","r")
except Exception as e:
    logging.error(e)
print("File error logged")

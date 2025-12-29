"""
Q6. Write a Python program that logs an error message when a division by zero exception occurs.
"""
import logging
logging.basicConfig(filename="error.log", level=logging.ERROR)
try:
    10/0
except ZeroDivisionError:
    logging.error("Division by zero occurred")
print("Error logged")

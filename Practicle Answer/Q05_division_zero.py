"""
Q5. How would you catch and handle a division by zero error in Python?
"""
try:
    print(10/0)
except ZeroDivisionError:
    print("Division by zero error occurred.")

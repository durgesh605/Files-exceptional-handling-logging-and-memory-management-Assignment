"""
Q8. Write a program to handle a file opening error using exception handling.
"""
try:
    open("abc.txt","r")
except Exception as e:
    print("Error:", e)

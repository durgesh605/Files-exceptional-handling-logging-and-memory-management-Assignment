"""
Q3. How would you handle a case where the file does not exist while trying to open it for reading?
"""
try:
    open("nofile.txt","r")
except FileNotFoundError:
    print("File does not exist.")

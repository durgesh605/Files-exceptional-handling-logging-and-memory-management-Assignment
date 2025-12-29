"""
Q20. How would you open a file and read its contents using a context manager in Python?
"""
with open("sample.txt","r") as f:
    print(f.read())

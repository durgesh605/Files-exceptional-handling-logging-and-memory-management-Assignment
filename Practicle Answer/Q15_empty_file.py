"""
Q15. Write a Python program that prints the content of a file and handles the case when the file is empty.
"""
try:
    with open("empty.txt","r") as f:
        content=f.read()
        if not content:
            print("File is empty")
        else:
            print(content)
except FileNotFoundError:
    print("File not found")

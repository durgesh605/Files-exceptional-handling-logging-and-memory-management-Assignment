"""
Q1. How can you open a file for writing in Python and write a string to it?
"""
with open("sample.txt","w") as f:
    f.write("Hello, this is a sample file.")
print("Q1 executed")

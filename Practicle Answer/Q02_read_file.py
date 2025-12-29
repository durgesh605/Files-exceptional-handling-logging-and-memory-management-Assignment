"""
Q2. Write a Python program to read the contents of a file and print each line.
"""
with open("sample.txt","r") as f:
    for line in f:
        print(line.strip())

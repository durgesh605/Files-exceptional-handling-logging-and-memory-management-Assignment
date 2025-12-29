"""
Q21. Write a Python program that reads a file and prints the number of occurrences of a specific word.
"""
count=0
with open("sample.txt","r") as f:
    for line in f:
        count+=line.count("sample")
print(count)

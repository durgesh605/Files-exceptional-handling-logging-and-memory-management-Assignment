"""
Q4. Write a Python script that reads data from one file and writes its content to another file.
"""
with open("sample.txt","r") as src, open("copy.txt","w") as dest:
    dest.write(src.read())
print("File copied")

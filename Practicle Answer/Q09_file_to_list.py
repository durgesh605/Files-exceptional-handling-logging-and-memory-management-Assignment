"""
Q9. How can you read a file line by line and store its contents in a list?
"""
with open("sample.txt","r") as f:
    lines=f.readlines()
print(lines)

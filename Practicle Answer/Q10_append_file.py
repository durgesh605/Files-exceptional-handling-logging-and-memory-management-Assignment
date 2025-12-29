"""
Q10. How can you append data to an existing file in Python?
"""
with open("sample.txt","a") as f:
    f.write("\nThis is appended data.")
print("Data appended")

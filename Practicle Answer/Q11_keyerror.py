"""
Q11. Write a Python program to handle a KeyError in a dictionary.
"""
data={"a":1}
try:
    print(data["b"])
except KeyError:
    print("Key not found")

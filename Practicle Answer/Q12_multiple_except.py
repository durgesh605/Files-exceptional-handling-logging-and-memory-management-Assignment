"""
Q12. Write a program that demonstrates using multiple except blocks.
"""
try:
    int("abc")
except ValueError:
    print("ValueError occurred")
except TypeError:
    print("TypeError occurred")

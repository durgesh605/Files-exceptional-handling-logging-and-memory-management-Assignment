"""
Q17. Write a Python program to create and write a list of numbers to a file, one number per line.
"""
nums=[1,2,3,4,5]
with open("numbers.txt","w") as f:
    for n in nums:
        f.write(str(n)+"\n")
print("Numbers written")

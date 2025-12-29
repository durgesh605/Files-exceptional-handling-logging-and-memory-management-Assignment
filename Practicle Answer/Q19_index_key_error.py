"""
Q19. Write a program that handles both IndexError and KeyError using a try-except block.
"""
lst=[1,2]
d={"x":10}
try:
    print(lst[5])
    print(d["y"])
except (IndexError,KeyError) as e:
    print("Error:",e)

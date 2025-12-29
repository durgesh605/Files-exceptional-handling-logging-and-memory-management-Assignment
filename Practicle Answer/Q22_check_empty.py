"""
Q22. How can you check if a file is empty before attempting to read its contents?
"""
import os
print(os.path.getsize("sample.txt")==0)

"""
Q16. Demonstrate how to use memory profiling to check the memory usage of a small Python program.
"""
import tracemalloc
tracemalloc.start()
data=[i for i in range(10000)]
print(tracemalloc.get_traced_memory())
tracemalloc.stop()

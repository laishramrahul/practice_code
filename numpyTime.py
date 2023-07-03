import numpy as np
import timeit
# Simple mathematics first
x = np.arange(4)
print("x     =", x)
print("x + 5 =", x + 5)
print("x - 5 =", x - 5)
print("x * 2 =", x * 2)
print("x / 2 =", x / 2)
# Divide and round
print("x // 2 =", x // 2)  

def calculate_inverse(values):    
    output = np.empty(len(values))    
    for i in range(len(values)):        
        output[i] = 1.0 / values[i]    
    return output       

values = np.random.randint(1, 10, size=5)
print(calculate_inverse(values))

large_array = np.random.randint(1, 100, size=1000000)

# This is a Jupyter notebook tool to measure the execution
# time of an instruction
print(timeit.timeit(calculate_inverse(large_array)))
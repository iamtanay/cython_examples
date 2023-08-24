import pandas as pd
import numpy as np
import time
from moving_average_cython import calculate_moving_average_cython

# Generate sample DataFrame
data = {'values': np.random.rand(10000000)}
df = pd.DataFrame(data)

window_size = 10

# Measure time taken by pandas implementation
start_time = time.time()
pandas_result = df['values'].rolling(window=window_size).mean()
pandas_time = time.time() - start_time

# Measure time taken by Cython implementation
start_time = time.time()
cython_result = calculate_moving_average_cython(df['values'].values, window_size)
cython_time = time.time() - start_time

# Print the first few rows of both results
# print("Pandas result:")
# print(pandas_result[11:20])
# print("\nCython result:")
# print(cython_result[:10])

# Print execution times
print(f"Pandas time: {pandas_time:.6f} seconds")
print(f"Cython time: {cython_time:.6f} seconds")
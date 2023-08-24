import numpy as np
from datetime import datetime
from datetime_example import calculate_time_difference

# Generate sample data
date_strings = ["2023-08-01", "2023-08-05", "2023-08-10", "2023-08-15"]
reference_date_str = "2023-08-08"

# Convert date strings to datetime objects
date_objects = [datetime.strptime(date, "%Y-%m-%d") for date in date_strings]

# Convert datetime objects to string representations
date_strings_cython = np.array([date.strftime("%Y-%m-%d") for date in date_objects], dtype=object)

# Calculate time differences using Cython
time_diffs = calculate_time_difference(date_strings_cython, reference_date_str)

# Print results
print("Date strings:")
print(date_strings)
print("Time differences:")
print(time_diffs)
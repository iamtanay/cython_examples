from variable_types import use_all_data_types

# Call the Cython function
result = use_all_data_types(5)

# Print the results
print("Results from Cython:")
print("Integer:", result[0])
print("String:", result[1])
print("Double:", result[2])
print("Datetime:", result[3])
print("Cython class value:", result[4])
print("NumPy array:", result[5])
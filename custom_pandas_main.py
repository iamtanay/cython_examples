import pandas as pd
import numpy as np
from custom_pandas import CustomSeries, CustomDataFrame

# Generate sample data
data = {'A': np.random.rand(100000), 'B': np.random.rand(100000)}
custom_dataframe_data = {'A': CustomSeries(data['A']), 'B': CustomSeries(data['B'])}

# Create pandas DataFrame
pandas_dataframe = pd.DataFrame(data)

# Create custom DataFrame
custom_dataframe = CustomDataFrame(custom_dataframe_data)

# Access and print data from pandas DataFrame
print("Pandas DataFrame:")
print(pandas_dataframe.head())

# Access and print data from custom DataFrame
print("\nCustom DataFrame:")
print(custom_dataframe['B'][0])
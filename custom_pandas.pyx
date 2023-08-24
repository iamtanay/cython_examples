# Import required libraries
cimport numpy as cnp

# Define custom Series class
cdef class CustomSeries:
    cdef cnp.ndarray data

    def __init__(self, cnp.ndarray data):
        self.data = data

    def __getitem__(self, int idx):
        return self.data[idx]

# Define custom DataFrame class
cdef class CustomDataFrame:
    cdef dict data

    def __init__(self, dict data):
        self.data = data

    def __getitem__(self, str col_name):
        return self.data[col_name]
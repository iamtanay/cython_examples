# Import required libraries
import numpy as np
cimport numpy as cnp
from datetime import datetime, timedelta
from cpython.datetime cimport datetime

# Define the Cython function
def calculate_time_difference(cnp.ndarray[object, ndim=1] date_strings, object reference_date_str):
    cdef Py_ssize_t n = date_strings.shape[0]
    cdef cnp.ndarray[double, ndim=1] time_diffs = np.empty(n)

    cdef int i
    cdef datetime reference_date = datetime.strptime(reference_date_str, "%Y-%m-%d")

    for i in range(n):
        date = datetime.strptime(date_strings[i], "%Y-%m-%d")
        time_diff = (date - reference_date).days
        time_diffs[i] = time_diff

    return time_diffs
import numpy as np
cimport numpy as cnp

def calculate_moving_average_cython(cnp.ndarray[cnp.double_t, ndim=1] data, int window):
    cdef Py_ssize_t n = data.shape[0]
    cdef cnp.ndarray[cnp.double_t, ndim=1] result = np.empty(n)

    cdef int i
    cdef double running_sum = 0.0

    for i in range(n):
        running_sum += data[i]
        if i >= window:
            running_sum -= data[i - window]
            result[i - window + 1] = running_sum / window
        else:
            result[i] = running_sum / (i + 1)

    return result
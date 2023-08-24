import c_primes
import time

#print(c_primes.prime_finder(5))

start_python_function = time.time()
c_primes.prime_finder(20000)
end_python_function = time.time()

print(end_python_function - start_python_function)

start_cython_function = time.time()
c_primes.prime_optimized(20000)
end_cython_function = time.time()

print(end_cython_function - start_cython_function)

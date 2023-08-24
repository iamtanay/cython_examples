def prime_finder(amount):
    primes = []

    found = 0
    number = 2
    while found < amount:
        for x in primes:
            if number % x == 0:
                break

        else:
            primes.append(number)
            found+=1
        
        number+=1
    return primes

def prime_optimized(int nb_primes):
    cdef int n, i, len_p
    cdef int[100000] p

    if nb_primes > 100000:
        nb_primes = 100000

    len_p = 0  # The current number of elements in p.
    n = 2
    while len_p < nb_primes:
        # Is n prime?
        for i in p[:len_p]:
            if n % i == 0:
                break

        # If no break occurred in the loop, we have a prime.
        else:
            p[len_p] = n
            len_p += 1
        n += 1

    # Let's copy the result into a Python list:
    result_as_list = [prime for prime in p[:len_p]]
    return result_as_list
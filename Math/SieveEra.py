def list_primes(n):
    from math import ceil
    '''
    Returns a list of primes less than n.
    Returns None for n <= 1.
    '''
    if n <= 1:
        return
    elif type(n) != int:
        raise TypeError

    else:

        primes = [True for i in range(n)]
        primes[0] = primes[1] = False

        for p in range(2, n):
            if primes[p] == True:
                primes[p**2 : n : p] = [False for j in range(ceil((n-p**2)/p))]

        return [i for i in range(n) if primes[i]]



def list_primes_watch(n):
    from math import ceil
    from time import perf_counter as pc
    '''
    Returns a list of primes less than n.
    Returns None for n <= 1.
    '''
    if n <= 1:
        return
    elif type(n) != int:
        raise TypeError

    else:
        start = pc()
        primes = [True for i in range(n)]
        primes[0] = primes[1] = False

        for p in range(2, int(n**0.5) + 1):
            if primes[p] == True:
                primes[p**2 : n : p] = [False for j in range(ceil((n-p**2)/p))]
        end = pc()

        return ([i for i in range(n) if primes[i]], f'{round((end - start)*1000, 4)} ms')



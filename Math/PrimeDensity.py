from SieveEra import list_primes

def prime_density(n):
    primes = list_primes(n)
    return len(primes)/n

def prime_density_plot(n):
    import matplotlib.pyplot as plt

    x = [i for i in range(2, n)]
    y = []
    for i in x:
        y.append(prime_density(i))
    plt.plot(x, y)
    plt.xlabel("n")
    plt.ylabel("prime_density(n)")
    plt.show()

prime_density_plot(1000)


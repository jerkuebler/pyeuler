def numprime(position):

    primes = [2]
    i = 3

    while len(primes) < position:
        if all(i % j != 0 for j in primes):
            primes.append(i)
        i += 2

    return primes[position - 1]


print(numprime(10001))

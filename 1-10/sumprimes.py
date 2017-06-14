# Run time greater than 15 minutes


def sumprime(below):
    primes = [2]
    i = 3

    while i < below:
        if all(i % j != 0 for j in primes):
            primes.append(i)
        i += 2

    return sum(primes)


print(sumprime(2000000))

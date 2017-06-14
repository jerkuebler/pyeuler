# Run time less than 5 seconds


def sumprime(below):

    total = 0

    sieve = [True] * (below+1)

    for p in range(2, below):
        if sieve[p]:
            total += p
            for i in range(p*p, below, p):
                sieve[i] = False

    return total


print(sumprime(2000000))
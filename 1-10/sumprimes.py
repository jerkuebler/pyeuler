def sumprime(below):

    primes = [2]
    i = 3
    recent = 0

    while recent < below:
        if all(i % j != 0 for j in primes):
            primes.append(i)
            recent = i
            print(recent)
        i += 2

    return sum(primes)


print(sumprime(2000000))
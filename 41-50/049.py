from itertools import permutations


def prime(n):
    if n < 2:
        return False

    for i in range(2, int(n ** 0.5 + 1)):
        if n % i == 0:
            return False

    return True


primes = [x for x in range(1000, 10000) if prime(x)]

for prime in primes:
    check = (int(''.join(x)) for x in set(permutations(str(prime))) if int(''.join(x)) in primes)
    seq = sorted([x for x in check if x in [prime, prime + 3330, prime + 6660]])
    if len(seq) > 2:
        print(seq)
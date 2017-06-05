from math import sqrt


def prime(n):

    if n < 2:
        return False

    for i in range(2, int(sqrt(n) + 1)):
        if n % i == 0:
            return False

    return True


def factor(n):

    factors = []

    for i in range(2, int(sqrt(n) + 1)):
        if n % i == 0 and prime(i):
                factors.append(i)

    return factors

print(factor(600851475143))

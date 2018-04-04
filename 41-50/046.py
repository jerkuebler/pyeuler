def prime(n):
    if n < 2:
        return False

    for i in range(2, int(n ** 0.5 + 1)):
        if n % i == 0:
            return False

    return True


def goldbach(num):
    max_prime = num - 2
    primes = [x for x in range(max_prime + 1) if prime(x)]

    for i in primes:
        test = ((num - i) / 2) ** 0.5
        if int(test) == test:
            return True

    return False


def natural_numbers():
    i = 1
    while True:
        i += 1
        yield i


if __name__ == '__main__':
    composites = (x for x in natural_numbers() if x % 2 != 0 and not prime(x))
    gold = True
    num = 0
    while gold is True:
        num = next(composites)
        gold = goldbach(num)

    print(num)

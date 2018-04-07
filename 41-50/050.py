def prime(n):
    if n < 2:
        return False

    for i in range(2, int(n ** 0.5 + 1)):
        if n % i == 0:
            return False

    return True


def remove_highest(prime_list):
    prime_sum = sum(prime_list)
    while not prime(prime_sum):
        prime_sum -= consecutive_primes.pop()

    return prime_list


def remove_lowest(prime_list):
    prime_sum = sum(prime_list)
    while not prime(prime_sum):
        prime_sum -= consecutive_primes[0]
        del (consecutive_primes[0])

    return prime_list


if __name__ == '__main__':
    primes = (x for x in range(10000) if prime(x))

    max_prime = 0
    current = next(primes)
    consecutive_primes = []
    while max_prime + current < 1000000:
        max_prime += current
        consecutive_primes.append(current)
        current = next(primes)

    lowest = remove_lowest(consecutive_primes)
    highest = remove_highest(consecutive_primes)

    if len(lowest) > len(highest):
        print(sum(lowest))
    else:
        print(sum(highest))

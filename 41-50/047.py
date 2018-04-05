def natural_numbers():
    i = 1
    while True:
        i += 1
        yield i


def prime(n):
    if n < 2:
        return False

    for i in range(2, int(n ** 0.5 + 1)):
        if n % i == 0:
            return False

    return True


def prime_factors(n):
    factors = []

    while not prime(n):
        for i in range(2, int(n)):
            if n % i == 0:
                n /= i
                factors.append(i)
                break

    factors.append(int(n))

    return factors


if __name__ == '__main__':

    chain_length = 0
    current_facts = []
    for i in natural_numbers():
        facts = prime_factors(i)
        if len(set(facts)) > 3 and not any(facts) in current_facts:
            chain_length += 1
            current_facts.extend(facts)
        else:
            chain_length = 0
            current_facts = []

        if chain_length == 4:
            print(i - 3)
            break

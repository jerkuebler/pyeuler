def prime(n):
    if n < 2:
        return False

    for i in range(2, int(n ** 0.5 + 1)):
        if n % i == 0:
            return False

    return True


def getprime(above, below):
    max_factor = below ** 0.5

    sieve = [True] * below

    for p in range(2, int(max_factor)):
        if sieve[p]:
            for i in range(p * p, below, p):
                sieve[i] = False

    for i in range(above, len(sieve)):
        if sieve[i]:
            yield i


def check_replacements(dig, target):
    replacement_nums = [int(target.replace(dig, str(i))) for i in range(int(dig), 10)]

    if sum(map(prime, replacement_nums)) > 7:
        return True

    return False


def check_primes():
    target_nums = ['0', '1', '2']
    primes = [num for num in getprime(above=9999, below=1000000)]

    for num in primes:
        str_num = str(num)

        for digit in str_num:
            if digit in target_nums and check_replacements(digit, str_num):
                return num


if __name__ == "__main__":
    print(check_primes())

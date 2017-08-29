# This is an example of needing to know an obscure math rule; any number whose digits add to a number that is divisible
# by 3 is also divisible by 3. Easy to then see that, going through the pandigital numbers, only those of length 4 and
# 7 are capable of being prime. Therefore, look for primes up to the maximum 7 digit pandigital number.

def largest_pandigital_prime():

    primes = getprime(7654321)

    largest = 0
    for i in primes:
        if pandigital(i, len(str(i))):
            largest = i

    return largest


def pandigital(a, length):
    num_list = "123456789"
    full_num = ''.join(sorted(str(a)))
    if full_num == num_list[:length]:
        return True
    else:
        return False

def getprime(below):

    max_factor = below ** 0.5

    sieve = [True] * below
    primes = []

    for p in range(2, int(max_factor)):
        if sieve[p]:
            for i in range(p*p, below, p):
                sieve[i] = False

    for i in range(2, len(sieve)):
        if sieve[i]:
            primes.append(i)

    return primes

print(largest_pandigital_prime())

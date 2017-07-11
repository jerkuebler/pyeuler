# This version works absurdly quickly. Abuses Fermat's Little Theorem. Less about programming knowledge and more knowing
# the correct formula. Might be better split into ~4 functions?

def prime_sieve(below):
    prime_list = []
    safe_prime_list = []
    # Use a sieve to find primes.
    sieve = [True] * (below + 1)

    for p in range(2, below):
        if sieve[p]:
            for i in range(p * p, below, p):
                sieve[i] = False
    # Make a list of the prime numbers
    for j, k in enumerate(sieve):
        if k is True:
            prime_list.append(j)
    # Collect the safe primes in the list
    for num in prime_list:
        if (num * 2 + 1) in prime_list:
            safe_prime_list.append(num * 2 + 1)

    # Check if each safe prime is a full reptend prime, from largest to smallest
    for num in safe_prime_list[::-1]:
        period = 1
        while pow(10, period, num) != 1:
            period += 1
        if num - 1 == period:
            return num


print(prime_sieve(1000))


# Before I learned what Fermat's Little Theorem was, I attempted to solve the problem here. Ultimately, this method
# fails because you can't get python to display enough digits. That said, it would have an atrocious run time, even if
# you could print out 3000 decimal places.

def find_recurrence(num):
    recip_num = 1 / num
    format(recip_num, '.64g')
    print(recip_num)
    i = 2
    n = 1
    j = 0

    while n != 0:
        test_num = str(recip_num)[i:i + n]
        test_num_available = str(recip_num)[i + n:]
        test_recur = str(recip_num)[i + n:i + n * 2]
        if test_num in test_num_available:
            j += 1
            if test_num == test_recur:
                n = 0
            else:
                n += 1
        else:
            i += 1

    return j


def check_nums(max_num):
    max_len = 0
    recip_num = 0

    for num in range(1, max_num):
        new_len = find_recurrence(num)
        print(new_len)
        if new_len > max_len:
            max_len = new_len
            recip_num = num

    return recip_num, max_len

import math


def circ_prime(num):
    rotation = []
    str_num = str(num)

    for i in range(len(str_num)):
        rearranged_1 = str_num[i + 1:]
        rearranged_2 = str_num[:i + 1]
        rearranged = int(rearranged_1 + rearranged_2)
        rotation.append(rearranged)

    return rotation


def is_prime(list_nums):
    for n in list_nums:
        if n < 2:
            return False

        for i in range(2, int(math.sqrt(n) + 1)):
            if n % i == 0:
                return False

    return True


def main(max_num):

    circle_primes = []

    for num in range(max_num + 1):
        if is_prime(circ_prime(num)):
            circle_primes.append(num)

    return circle_primes

circ_primes = main(1000000)
print(circ_primes)
print(len(circ_primes))

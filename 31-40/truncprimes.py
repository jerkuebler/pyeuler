# Under 1 minute, but I'm not sure that would have been true on a weaker computer.

import math


def is_prime(n):

    if n < 2:
        return False

    for i in range(2, int(math.sqrt(n) + 1)):
        if n % i == 0:
            return False

    return True


def check_nums(expected_primes):
    num_list = []
    i = 9

    while len(num_list) < expected_primes:
        i += 1
        all_perms = []

        for num in range(len(str(i))):
            all_perms.append(int(str(i)[0:num + 1]))
            all_perms.append(int(str(i)[num - len(str(i)):len(str(i))]))

        set_perms = list(set(all_perms))

        for index, num in enumerate(set_perms):
            if is_prime(num):
                set_perms[index] = True
            else:
                set_perms[index] = False

        if all(set_perms):
            num_list.append(i)
    return num_list

print(sum(check_nums(11)))

# Don't reinvent the wheel?

import itertools


def find_lexi_perms(digits):

    return list(itertools.permutations(range(digits), digits))[999999]

print(find_lexi_perms(10))
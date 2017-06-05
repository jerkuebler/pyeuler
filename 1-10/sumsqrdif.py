def sumsqrdif(natnumbers):

    sum_sqr = sum(x ** 2 for x in range(1, natnumbers + 1))
    sqr_sum = sum(x for x in range(1, natnumbers + 1)) ** 2

    dif = sqr_sum - sum_sqr

    return dif

print(sumsqrdif(100))
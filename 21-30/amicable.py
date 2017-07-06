# Long run time due to nested loop in amicable_under function. Still under a minute.
# Problem occurred because numbers were being compared against themselves. range(i + 1, max_num + 1) on line 40 fixed.

memoize_sums = {}

def sum_proper_divisors(num):
    divis = [1]

    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            divis.append(i)
            divis.append(num // i)
    divis = set(divis)
    memoize_sums[num] = sum(divis)

    return sum(divis)


def is_amicable(num1, num2):

    if num2 in memoize_sums:
        check1 = num1 == memoize_sums[num2]
    else:
        check1 = num1 == sum_proper_divisors(num2)
    if num1 in memoize_sums:
        check2 = num2 == memoize_sums[num1]
    else:
        check2 = num2 == sum_proper_divisors(num1)

    if check1 and check2:
        return True
    else:
        return False


def amicable_under(max_num):
    amicable_nums = []

    for i in range(2, max_num + 1):
        for j in range(i + 1, max_num + 1):
            if is_amicable(i, j):
                amicable_nums.append(i)
                amicable_nums.append(j)

    return amicable_nums


print(sum(set(amicable_under(10000))))

def sum_proper_divisors(num):
    divis = [1]

    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            divis.append(i)
            divis.append(num // i)
    divis = set(divis)

    if sum(divis) > num:
        return True
    else:
        return False

def sum_of_abundance(num):

    for i in range(1, num):
        if sum_proper_divisors(i):
            if sum_proper_divisors(num - i):
                return True

    return False

def sum_of_non_abundant_sums(maxnum):

    total = 0

    for num in range(maxnum + 1):
        if not sum_of_abundance(num):
            total += num

    return total

print(sum_of_non_abundant_sums(28123))

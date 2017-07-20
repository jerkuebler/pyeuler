# Played with it till it functioned for all numbers 1-9


def pandigital(a, b, prod, length):
    num_list = "123456789"
    full_num = ''.join(sorted(str(a) + str(b) + str(prod)))
    if full_num == num_list[:length]:
        return True
    else:
        return False


def check_range(pandigital_length):
    pandigital_list = []
    pandigital_sum = []
    check_length = int(pandigital_length ** .5)
    check_str = "987654321"

    # All pandigital numbers must be 9 digits, so need to be multiplying 3-4 digit terms by 1-2 digit terms.
    for a in range(int(check_str[:check_length + 1])):
        for b in range(int(check_str[:check_length - 1] or 1)):
            if pandigital(a, b, (a * b), pandigital_length):
                pandigital_list.append((a, b, (a * b)))
                pandigital_sum.append((a * b))

    return pandigital_list, sum(set(pandigital_sum))


print(check_range(9))

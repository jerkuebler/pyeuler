def digit_fifth_power(num):
    return num == sum((int(x) ** 5 for x in str(num)))


def find_fifth_digit_sums(range_max):
    sums_list = []

    for num in range(2, range_max):
        if digit_fifth_power(num):
            sums_list.append(num)

    return sums_list


print(sum(find_fifth_digit_sums(1000000)))

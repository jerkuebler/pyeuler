from math import sqrt


def prime(n):
    if n < 2:
        return False

    for i in range(2, int(sqrt(n) + 1)):
        if n % i == 0:
            return False

    return True


def quad_form(num, a, b):
    return num ** 2 + a * num + b


def quad_primes(range_width):
    start_a = - range_width + 1
    end_a = range_width
    start_b = -range_width
    end_b = range_width + 1
    answer_dict = {}

    for a in range(start_a, end_a):
        for b in range(start_b, end_b):
            n = 0
            while prime(quad_form(n, a, b)):
                n += 1
            answer_dict[n] = (a, b)

    max_n = max(x for x in answer_dict)
    answer = answer_dict[max_n][0] * answer_dict[max_n][1]
    return max_n, answer_dict[max_n], answer


print(quad_primes(1000))

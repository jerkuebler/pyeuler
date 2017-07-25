# Short list.

import math


def digit_factorials(num):

    total = 0

    for i in str(num):
        fact = math.factorial(int(i))
        total += fact

    if total == num:
        return True

    return False

def check_numbers():

    digit_fact_list = []
    for i in range(3, 362880):
        if digit_factorials(i):
            digit_fact_list.append(i)

    return digit_fact_list

digit_fact = check_numbers()
print(digit_fact)
print(sum(digit_fact))
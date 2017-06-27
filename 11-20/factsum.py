import math


def cheap_solution(fact):

    i = math.factorial(fact)
    digits = str(i).split()
    return sum(int(x) for x in digits)

print(cheap_solution(100))
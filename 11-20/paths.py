import math


def paths(side):

    return (math.factorial(2*side)/(math.factorial(side))) / math.factorial(2 * side - side)

print(paths(20))

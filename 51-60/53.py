# Can also use math.factorial here
def factorial(num):
    if num == 1:
        return 1
    else:
        return num * factorial(num - 1)


def combinatoric_value(n, r):
    return factorial(n) / (factorial(r) * factorial(n - r))


def selections_above(longest, above):
    total = 0
    for i in range(longest + 1):
        for j in range(1, i):
            if combinatoric_value(i, j) > above:
                total += 1

    return total


if __name__ == "__main__":
    print(selections_above(100, 1000000))

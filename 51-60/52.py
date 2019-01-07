def multi_contains_digits(num, multi=2, target=6):
    if sorted(str(num)) == sorted(str(num * multi)):
        print(multi, "  :  ", num * multi)
        if multi < target:
            return multi_contains_digits(num, multi + 1)
        else:
            return True

    return False


def permuted_multiples():
    n = 1
    while not multi_contains_digits(n):
        n += 1
        print(n)

    return n


if __name__ == "__main__":
    print("Problem 52 answer is: ", permuted_multiples())

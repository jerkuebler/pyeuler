import itertools

total_sub = 0
primes = [2, 3, 5, 7, 11, 13, 17]
for num in itertools.permutations('0123456789'):

    str_num = ''.join(num)
    tests = [int(str_num[x + 1: x + 4]) % primes[x] == 0 for x in range(7)]

    if all(tests):
        total_sub += int(str_num)

print(total_sub)

import collections


def triangle_num(n):
    return n * (n + 1) / 2


def pentagonal_num(n):
    return n * (3 * n - 1) / 2


def hexagonal_num(n):
    return n * (2 * n - 1)


h = 200
nums = []
result = []

while len(result) < 2:

    for i in range(h - 198, h):
        nums.extend((triangle_num(i), pentagonal_num(i), hexagonal_num(i)))

    counter = collections.Counter(nums)
    result = [(key, counter[key]) for key in counter if counter[key] > 2]
    h += 200

print(result)

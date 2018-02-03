import math


pentagonal = []
for num in range(1, 4100):
    pentagonal.append(num * (3 * num - 1) / 2)

d = math.inf
for j in range(4000):
    for i in range(j):
        subtraction = pentagonal[j] - pentagonal[i]
        if subtraction in pentagonal[:j]:
            addition = pentagonal[j] + pentagonal[i]
            if addition in pentagonal[j:]:
                value = abs(subtraction)
                if value < d:
                    print(value)
                    quit()

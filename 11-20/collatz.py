def collatz_generator(start):

    sequence = []

    while start != 1:
        sequence.append(start)
        if start % 2 == 0:
            start /= 2
        else:
            start = 3 * start + 1

    return sequence

def longest_sequence(largest_start):

    sequence = []

    for num in range(largest_start, largest_start//2, -1):
        testseq = collatz_generator(num)
        if len(testseq) > len(sequence):
            sequence = testseq

    return sequence

print(longest_sequence(1000000))
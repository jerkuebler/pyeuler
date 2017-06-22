def prepnums(numfile):
    finalnums = []

    with open(numfile, 'r') as nums:
        for item in nums:
            finalgrid.append(int(item))

    return finalnums

print(str(sum(prepnums('largesum.txt')))[:10])

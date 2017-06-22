def prepnums(numfile):
    finalgrid = []

    with open(numfile, 'r') as nums:
        for item in nums:
            finalgrid.append(int(item))

    return finalgrid

print(str(sum(prepnums('largesum.txt')))[:10])
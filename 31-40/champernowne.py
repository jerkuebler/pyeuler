# Could also leave out the pre-decimal part to use less code, but then it wouldn't be Champernowne's Constant


def champernowne(len_champ):

    champ = '0.'

    for i in range(1, len_champ + 1):
        champ += str(i)

    sections = [1, 10, 100, 1000, 10000, 100000, 1000000]
    fractional_mod = 1
    champ_prod = 1

    for j in sections:
        champ_prod *= int(champ[j + fractional_mod])

    return champ_prod

print(champernowne(1000000))

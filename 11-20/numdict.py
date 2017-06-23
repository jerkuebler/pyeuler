num_dict = {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine',
            10: 'ten', 11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen', 15: 'fifteen', 16: 'sixteen',
            17: 'seventeen', 18: 'eighteen', 19: 'nineteen', 0: ''}
tens_dict = {'2': 'twenty', '3': 'thirty', '4': 'forty', '5': 'fifty', '6': 'sixty', '7': 'seventy', '8': 'eighty',
             '9': 'ninety'}

def num_let_count(number):

    str_num = str(number)
    
    def tens_place(twodigits):
        if twodigits[0] == '1':
            return len(num_dict[int(twodigits)])
        elif twodigits[1] == 0:
            return len(tens_dict[twodigits[0]])
        else:
            return len(tens_dict[twodigits[0]] + num_dict[int(twodigits[1])])

    if len(str_num) == 1:
        return len(num_dict[number])
    elif len(str_num) == 2:
        return tens_place(str_num)
    elif len(str_num) == 3:
        if str_num[1] == '0':
            if str_num[2] == '0':
                return len(num_dict[int(str_num[0])] + 'hundred')
            else:
                return len(num_dict[int(str_num[0])] + 'hundredand' + num_dict[int(str_num[2])])
        else:
            return len(num_dict[int(str_num[0])] + 'hundredand') + tens_place(str_num[1:3])
    elif len(str_num) == 4:
        return len('onethousand')
    

def count_em(upto):

    total = 0

    for num in range(1, upto + 1):
        print(num)
        print(num_let_count(num))
        total += num_let_count(num)

    return total

print(count_em(1000))
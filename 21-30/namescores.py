def score_name(name):
    name = name.lower()
    return sum((ord(char) - 96 for char in name))


def get_scores(names_file):
    scores_sum = 0

    with open(names_file) as name_list:
        for line in name_list:
            names = line.split(',')
            names = sorted(names)

        for i, name in enumerate(names):
            scores_sum += score_name(name[1:-1]) * (i + 1)

    return scores_sum


print(get_scores('names.txt'))

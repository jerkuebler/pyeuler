# Figure out how the diagonals are related. Can be used for any size spiral.


def sum_diagonal(max_side_length):
    diagonal_sum = 1

    for side_length in range(3, max_side_length + 1, 2):
        # down-right diagonal
        diagonal_sum += (side_length - 2) ** 2 + side_length - 2

        # down-left diagonal
        diagonal_sum += (side_length - 2) ** 2 + 2 * side_length - 2

        # up-left diagonal
        diagonal_sum += (side_length - 2) ** 2 + 3 * side_length - 2

        # up-right diagonal
        diagonal_sum += side_length ** 2

    return diagonal_sum


print(sum_diagonal(1001))

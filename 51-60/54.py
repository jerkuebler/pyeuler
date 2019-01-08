CARDS = {
    'T': 10,
    'J': 11,
    'Q': 12,
    'K': 13,
    'A': 14,
}

HANDS = {
    "High Card": 1,
    "One Pair": 2,
    "Two Pairs": 3,
    "Three of a Kind": 4,
    "Straight": 5,
    "Flush": 6,
    "Full House": 7,
    "Four of a Kind": 8,
    "Straight Flush": 9,
    "Royal Flush": 10
}


def duplicate_values(hand):
    values = [card["value"] for card in hand]
    counts = [values.count(value) for value in values]
    return values[counts.index(max(counts))], max(counts)


def second_dup(value, hand):
    sub_hand = [card for card in hand if card['value'] != value]
    value, count = duplicate_values(sub_hand)
    if count > 1:
        return value, count
    else:
        return False


def get_value(card):
    value = int(CARDS.get(card[0], card[0]))
    return {"value": value, "suit": card[1]}


def evaluate_hand(hand, drop_value=None):
    if drop_value:
        values = [card for card in hand if card['value'] != drop_value]
        straight = None
        flush = None
    else:
        values = [get_value(card) for card in hand]
        sorted_values = sorted(values, key=lambda x: x['value'])
        straight = all(sorted_values[x]["value"] - 1 == sorted_values[x - 1]["value"] for x in range(1, len(values)))
        flush = all(value["suit"] == values[0]["suit"] for value in values)

    duplicate = duplicate_values(values)
    max_value = max((value["value"] for value in values))

    if flush:
        if straight:
            if min((value["value"] for value in values)) == 10:
                return values, "Royal Flush", max_value
            else:
                return values, "Straight Flush", max_value

    if duplicate[1] == 4:
        return values, "Four of a Kind", duplicate[0]

    if duplicate[1] == 3:
        second = second_dup(duplicate[0], values)
        if second:
            return values, "Full House", duplicate[0]

    if flush:
        return values, "Flush", max_value

    if straight:
        return values, "Straight", max_value

    if duplicate[1] == 3:
        return values, "Three of a Kind", duplicate[0]

    if duplicate[1] == 2:
        second = second_dup(duplicate[0], values)
        if second:
            return values, "Two Pairs", duplicate[0]
        else:
            return values, "One Pair", duplicate[0]

    return values, "High Card", max_value


def compare_hands(p1, p2, p1_drop=None, p2_drop=None):
    player_one = evaluate_hand(p1, drop_value=p1_drop)
    player_two = evaluate_hand(p2, drop_value=p2_drop)
    if HANDS[player_one[1]] > HANDS[player_two[1]]:
        return "Player One Win!"
    elif HANDS[player_one[1]] < HANDS[player_two[1]]:
        return "Player Two Win!"
    else:
        if player_one[2] > player_two[2]:
            return "Player One Win!"
        elif player_one[2] < player_two[2]:
            return "Player Two Win!"
        else:
            return compare_hands(player_one[0], player_two[0], p1_drop=player_one[2], p2_drop=player_two[2])


def check_file():
    with open("./p054_poker.txt") as hands:
        p1_win = 0
        for hand in hands:
            cards = hand.split()
            p1 = cards[:5]
            p2 = cards[5:]
            winner = compare_hands(p1, p2)
            if winner == "Player One Win!":
                p1_win += 1

            print(winner)

        print(p1_win)


if __name__ == "__main__":
    check_file()

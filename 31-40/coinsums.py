# Can use a formula to solve this but it's far less satisfying than seeing the massive list of combinations

original_run = {'200': 0, "100": 0, "50": 0, "20": 0, "10": 0, "5": 0, "2": 0, "1": 0}
original_coin_list = [200, 100, 50, 20, 10, 5, 2, 1]
big_list = []


def count_coins(coin_list, total_amount, current_run):
    if coin_list:
        r = total_amount // coin_list[0]
        for i in range(r + 1):
            new_total = total_amount - (i * coin_list[0])
            current_run[str(coin_list[0])] = i
            new_list = coin_list[1:]
            if new_total == 0:
                big_list.append(current_run)
            elif total_amount > 0:
                count_coins(new_list, new_total, current_run)


count_coins(original_coin_list, 200, original_run)
print(big_list)
print(len(big_list))

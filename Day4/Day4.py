from typing import Tuple, List


def _scratch_worth(match_numbers: int) -> int:
    if match_numbers == 0:
        return 0
    else:
        return 2 ** (match_numbers - 1)


def _read_card(card_line: str) -> Tuple:
    numbers = card_line.split(":")[1]
    winners = numbers.split("|")[0].strip().split(" ")
    my_nums = numbers.split("|")[1].strip().split(" ")

    winners = list(filter(None, winners))
    my_nums = list(filter(None, my_nums))

    return winners, my_nums


def _list_count(winners: List, my_nums: List) -> int:
    nums = len([i for i in my_nums if i in winners])
    return nums


part2file = "inputDay4.txt"
card_dict = {}

with open(part2file, "r") as f:
    card_num = 1
    for line in f:
        card_dict[card_num] = 1
        card_num += 1

with open("inputDay4.txt", "r") as f:
    count = 0
    card_num = 1

    for line in f:
        card_line = line.rstrip()
        winners, my_nums = _read_card(card_line)
        nums = _list_count(winners, my_nums)
        count += _scratch_worth(nums)

        for i in range(card_num + 1, card_num + nums + 1):
            card_dict[i] += card_dict[card_num]

        card_num += 1

    print("Part 1:", count)
    print("Part 2:", sum(card_dict.values()))

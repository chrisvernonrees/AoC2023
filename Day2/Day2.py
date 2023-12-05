from typing import List

max_dict = {"red": 12, "green": 13, "blue": 14}


def _split_game(game: str) -> List:
    game = game.split(', ')
    split_game = []
    for hand in game:
        split_game.append(hand.split())
    return split_game


def _read_line(input_line: str) -> List:
    games = input_line.split(':')[1].strip().split(';')
    split_games = []
    for game in games:
        split_games.append(_split_game(game))
    return split_games


def _test_game(game: List) -> bool:
    test_flag = False
    for set in game:
        if int(set[0]) > max_dict[set[1]]:
            test_flag = True
    return test_flag


def _get_min_power(game: List) -> int:
    min_dict = {"red": 0, "green": 0, "blue": 0}
    flat_list = [item for sublist in game for item in sublist]
    for set in flat_list:
        min_dict[set[1]] = max(min_dict[set[1]], int(set[0]))
    return min_dict["red"] * min_dict["green"] * min_dict["blue"]


with open("inputDay2.txt", "r") as f:
    game_num = 1
    count = 0
    count_2 = 0
    for line in f:
        games = _read_line(line.strip())
        flag = False
        for game in games:
            if _test_game(game):
                flag = True

        if not flag:
            count += game_num

        count_2 += _get_min_power(games)
        game_num += 1

print("Part 1:", count)
print("Part 2:", count_2)

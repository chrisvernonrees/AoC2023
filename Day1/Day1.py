import string
import re
from typing import List, Union

alphabet = string.ascii_lowercase
replace_dict = {
    "1": "one",
    "2": "two",
    "3": "three",
    "4": "four",
    "5": "five",
    "6": "six",
    "7": "seven",
    "8": "eight",
    "9": "nine"

}


def _remove_letters(input_string: str) -> str:
    output_number = input_string.translate({ord(i): None for i in alphabet})
    return output_number


def _get_number(num_string: str) -> int:
    start_num = num_string[0]
    end_num = num_string[-1]
    output_num = int(start_num + end_num)
    return output_num


def _line_to_num(input_string: str) -> int:
    num_string = _remove_letters(input_string)
    output_num = _get_number(num_string)
    return output_num


def _find_num_strings(input_string: str) -> List[List[Union[int, str]]]:
    tuple_list = []

    for key in replace_dict:
        positions = [m.start() for m in re.finditer(replace_dict[key], input_string)]
        for position in positions:
            tuple_list.append([position, key])

    return tuple_list


def _replacer(input_string: str, position: int, new_char: str) -> str:
    new_string = input_string[:position] + new_char + input_string[position + 1:]
    return new_string


def _replace_nums(input_string: str) -> str:
    update_list = _find_num_strings(input_string)
    for pair in update_list:
        input_string = _replacer(input_string, pair[0], pair[1])

    return input_string


part1_count = 0
part2_count = 0

with open("inputDay1.txt", "r") as f:
    for line in f:
        part1_count += _line_to_num(line.rstrip())

        new_line = _replace_nums(line.rstrip())
        part2_count += _line_to_num(new_line)

print("Day 1 Part 1:", part1_count)
print("Day 1 Part 2:", part2_count)

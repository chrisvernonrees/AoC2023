import numpy as np
from typing import Tuple, List

num_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

input_list = []

with open("inputDay3.txt", "r") as f:
    for line in f:
        input_list.append(list(line.strip()))

input_mat = np.asarray(input_list)

row_size, col_size = np.shape(input_mat)


def _get_num(row: int, col: int) -> Tuple:
    output_num = ''
    count = 0
    coords = []

    while (col + count < col_size) and (input_mat[row, col + count] in num_list):
        output_num += input_mat[row, col + count]
        coords.append([row, col + count])
        count += 1

    return int(output_num), coords


def _get_num_dict() -> dict:
    num_dict = {}
    index = 1

    for row in range(row_size):
        for col in range(col_size):

            if input_mat[row, col] in num_list and (col == 0 or input_mat[row, col - 1] not in num_list):
                num, coords = _get_num(row, col)
                num_dict[index] = [num, coords]
                index += 1

    return num_dict


def _get_neigbours(row, col):
    return [[row - 1, col - 1], [row - 1, col], [row - 1, col + 1], [row, col - 1], [row, col + 1], [row + 1, col - 1],
            [
                row + 1, col], [row + 1, col + 1]]


num_dict = _get_num_dict()

part1_count = 0
part2_count = 0

for row in range(row_size):
    for col in range(col_size):
        if input_mat[row, col] != '.' and input_mat[row, col] not in num_list:
            neighbours = _get_neigbours(row, col)
            nums = []

            for index in num_dict:
                num = num_dict[index][0]
                coords = num_dict[index][1]
                if any(x in neighbours for x in coords):
                    part1_count += num
                    nums.append(num)

            if len(nums) == 2:
                part2_count += nums[0] * nums[1]

print("Day 3 Part 1:", part1_count)
print("Day 3 Part 2:", part2_count)

from typing import List
from math import ceil, floor

input_dict = {}

with open("inputDay6.txt", "r") as f:
    for line in f:
        line.strip()
        input_dict[line.split(":")[0]] = [int(num) for num in line.split(":")[1].strip().split()]

races = len(input_dict["Time"])


def record_beaters(time: int, distance: int) -> int:
    winners = 0
    winning_flag = False

    for i in range(time):
        speed = i
        remaining_time = time - i
        race_dist = speed * remaining_time

        if race_dist > distance:
            winners += 1
            winning_flag = True

        if race_dist <= distance and winning_flag:
            break

    return winners


def record_beaters_quad(time: int, distance: int) -> int:
    b = - time
    c = distance
    min = ceil((-b - (b ** 2 - 4 * c) ** 0.5) / 2)
    max = floor((-b + (b ** 2 - 4 * c) ** 0.5) / 2)
    return max - min + 1


def sum_to_str(input_list: List[int]) -> int:
    str_list = [str(num) for num in input_list]
    output_num = ""
    for i in str_list:
        output_num += i
    return int(output_num)

margin = 1

for race in range(races):
    time = input_dict["Time"][race]
    distance = input_dict["Distance"][race]
    margin *= record_beaters_quad(time, distance)


print("Day 6 Part 1:", margin)

print("Day 6 Part 2:", record_beaters_quad(sum_to_str(input_dict["Time"]), sum_to_str(input_dict["Distance"])))

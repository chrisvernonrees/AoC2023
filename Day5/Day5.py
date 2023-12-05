from typing import List
import time

t0 = time.time()

mapping_dict = {}

with open("inputDay5.txt", "r") as f:
    for line in f:

        line.strip()

        if "seeds" in line:
            seeds = [int(seed) for seed in line.replace("seeds: ", "").split()]

        elif " map:" in line:

            map_name = line.replace(":", "").strip()
            mapping_dict[map_name] = []

        elif len(line) != 1:
            map = [int(num) for num in line.split()]
            mapping_dict[map_name].append(map)

"""Part 1"""


def _run_through_map(maps: List, seed_num: int) -> int:
    for map in maps:
        shift_range = range(map[1], map[1] + map[2])
        if seed_num in shift_range:
            seed_num = seed_num - map[1] + map[0]
            break
    return seed_num


def _map_seeds(maps: List, seeds: List[int]) -> List[int]:
    new_list = []
    for seed in seeds:
        new_list.append(_run_through_map(maps, seed))
    return new_list


seeds1 = seeds

for key in mapping_dict:
    maps = mapping_dict[key]
    seeds1 = _map_seeds(maps, seeds1)

print("Part 1:", min(seeds1))

"""Part 2"""

seed_ranges = []

for i in range(int(len(seeds) / 2)):
    seed_ranges.append([seeds[i * 2], seeds[i * 2] + seeds[i * 2 + 1] - 1])


def _apply_range_split(seed_spread: List, edit_spread: List):
    shifted = [max(seed_spread[0], edit_spread[0]), min(seed_spread[1], edit_spread[1])]
    unshifted = []
    if seed_spread[0] < shifted[0]:
        unshifted.append([seed_spread[0], shifted[0] - 1])
    if seed_spread[1] > shifted[1]:
        unshifted.append([shifted[1] + 1, seed_spread[1]])
    return shifted, unshifted


def _apply_a_map(map, unmapped_ranges):
    shift_range = [map[1], map[1] + map[2] - 1]
    shift_amount = map[0] - map[1]

    new_shifted_ranges = []
    new_unshifted_ranges = []

    for range in unmapped_ranges:
        if shift_range[1] < range[0] or shift_range[0] > range[1]:
            new_unshifted_ranges.append(range)
        else:
            shifted, unshifted = _apply_range_split(range, shift_range)
            new_shifted_ranges.append([x + shift_amount for x in shifted])
            new_unshifted_ranges += unshifted

    return new_shifted_ranges, new_unshifted_ranges


def _apply_a_step(maps, input_ranges):
    shifted_ranges = []

    for map in maps:
        new_shifted_ranges, new_unshifted_ranges = _apply_a_map(map, input_ranges)
        shifted_ranges += new_shifted_ranges
        input_ranges = new_unshifted_ranges

    return shifted_ranges + input_ranges


test_seeds = seed_ranges

for key in mapping_dict:
    maps = mapping_dict[key]
    seed_ranges = _apply_a_step(maps, seed_ranges)

print("Part 2:", min([r[0] for r in seed_ranges]))

t1 = time.time()

print(t1 - t0)
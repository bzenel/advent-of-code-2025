import sys
from functools import cmp_to_key
from collections import deque

def compare_range(range_1, range_2):
    # print(f'comparing {range_1} to {range_2}')
    if range_1[1] < range_2[0]:
        return "exclusive"  # to the left
    if range_1[0] > range_2[1]:
        return "exclusive"  # to the right
    if range_1[0] >= range_2[0] and range_1[1] <= range_2[1]:
        return "subset"  # range_1 is a subset of range_2
    if range_1[0] <= range_2[0] and range_1[1] >= range_2[1]:
        return "superset"  # range_1 is a superset of range_2
    if range_1[0] == range_2[0] and range_1[1] == range_2[1]:
        return "equal"
    if (range_1[1] > range_2[0] and range_1[1] < range_2[1]) or (range_2[1] > range_1[0] and range_2[1] < range_1[1]):
        return "merge"
    if range_1[1] == range_2[0] or range_2[1] == range_1[0]:
        return "merge"
    print('Fail!')
    return "fail"

def compare_range_v2(range_1, range_2):
    # Simplified range compare
    # Assumes ranges are "in order"
    # print(f'comparing {range_1} to {range_2}')
    if range_1[1] < range_2[0]:
        return "exclusive"  # to the left
    if range_1[0] <= range_2[0] and range_1[1] >= range_2[1]:
        return "superset"  # range_1 is a superset of range_2
    if range_1[1] >= range_2[0] and range_1[1] <= range_2[1]:
        return "merge"
    print('Fail!')
    return "fail"

def range_compare(range_1, range_2):
    if range_1[0] < range_2[0]:
        return -1
    if range_1[0] > range_2[0]:
        return 1
    # range_1[0] == range_2[0]:
    if range_1[2] < range_2[2]:
        return 1
    if range_1[2] > range_2[2]:
        return -1
    # range_1[2] == range_2[2]
    return 0

def merge_range(range_1, range_2):
    low_end = min(range_1[0], range_2[0])
    high_end = max(range_1[1], range_2[1])
    return [low_end, high_end, (high_end-low_end+1)]

if __name__ == "__main__":
    print(f'starting...')

    with open(sys.argv[1]) as file_handle:
        content = file_handle.read()
    lines = content.strip().split('\n')

    print(f'read {len(lines)} lines')

    ranges = []
    ingredients = []
    range_flag = True
    for line in lines:
        if len(line) == 0:
            print('Found a newline')
            range_flag = False
            continue
        if range_flag:
            ranges.append(line)
        else:
            ingredients.append(int(line))

    print(f'Found {len(ranges)} ranges, {len(ingredients)} ingredients')

    range_sets = []
    for value in ranges:
        lower, higher = value.split('-')
        range_sets.append([int(lower), int(higher)])
        print(f'Found lower {lower}, higher {higher}', flush=True)
    print(f'range sets: {range_sets}')

    fresh_list = []
    for ingredient in ingredients:
        for range_val in range_sets:
            # print(f'ingredient: {ingredient}, lower {range_val[0]}, upper {range_val[1]}')
            if ingredient >= range_val[0] and ingredient <= range_val[1]:
                fresh_list.append(ingredient)
                break
    print(f'Fresh list: {fresh_list}')
    print(f'Found {len(fresh_list)} fresh items')
    fresh_set = set(fresh_list)
    print(f'Found {len(fresh_set)} unique fresh items')

    print('Part 2!')

    range_sets = []
    for value in ranges:
        lower, higher = value.split('-')
        range_tuple = [int(lower), int(higher), int(higher)-int(lower)+1]
        print(f'Found range: {range_tuple}', flush=True)
        range_sets.append(range_tuple)

    print(f'range sets: {range_sets}')

    range_sets.sort(key=cmp_to_key(range_compare))
    print(f'Sorted range sets: {range_sets}')

    # orig_set = range_sets.copy()
    # working_set = deque(range_sets)
    # final_set = []
    # while len(working_set) >= 2:
    #     new_set = []
    #     range_1 = working_set.popleft()
    #     did_merge = False
    #     while len(working_set) >= 1:
    #         range_2 = working_set.popleft()
    #         val = compare_range(range_1, range_2)
    #         if val == "exclusive":
    #             print(f'{range_1} is exclusive of {range_2}')
    #             new_set.append(range_2)
    #             continue
    #         if val == "equal":
    #             print(f'{range_1} is equal to {range_2}')
    #             break
    #         if val == "superset":
    #             print(f'{range_1} is a superset of {range_2}')
    #             break
    #         if val == "subset":
    #             print(f'{range_1} is a subset of {range_2}')
    #             new_set.append(range_2)
    #         if val == "merge":
    #             print(f'{range_1} and range2 {range_2} overlap')
    #             new_set.append(merge_range(range_1, range_2))
    #             did_merge = True
    #     if did_merge is False:
    #         final_set.append(range_1)
    #     working_set = deque(new_set)
    #     print(f'working set is now {working_set}')
    # final_set.append(working_set.popleft())

    working_set = deque(range_sets)
    final_set = deque([])

    current_range = working_set.popleft()
    while len(working_set) > 0:
        print(f'Looking at: {current_range}')
        next_range = working_set.popleft()
        result = compare_range_v2(current_range, next_range)
        if result == "exclusive":
            print(f'{current_range} is exclusive of {next_range}')
            final_set.append(current_range)
            working_set.appendleft(next_range)
        elif result == "merge":
            print(f'{current_range} and range2 {next_range} overlap')
            new_range = merge_range(current_range, next_range)
            working_set.appendleft(new_range)
        elif result == "superset":
            print(f'{current_range} is a superset of {next_range}')
            continue
        else:
            print(f'Unexpected result {result}')
        current_range = working_set.popleft()
    final_set.append(current_range)
    print(f'Final set: {final_set}')

    print(f'fresh is {sum([x[2] for x in final_set])}')





    

        
    
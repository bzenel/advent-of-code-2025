from curses import newwin
from operator import ne
from re import L
import sys

def dump_grid(grid):
    print('---------------')
    for line in grid:
        print(f'{line}')

def num_neighbors(grid, loc_y, loc_x) -> int:
    matrix = [
        [-1, -1,], [0, -1], [1, -1],
        [-1, 0], [1, 0],  # note that [0,0] is ignored
        [-1, 1], [0, 1], [1, 1]
    ]
    neighbor_count = 0  # handles self
    for m_y, m_x in matrix:
        x = loc_x + m_x
        y = loc_y + m_y
        if x < 0 or y < 0 or x >= len(grid[0]) or y >= len(grid):
            # print(f'invalid x {x} or y {y}')
            continue
        if grid[y][x] == '@':
            neighbor_count += 1
    return neighbor_count

if __name__ == "__main__":
    print(f'starting...')

    with open(sys.argv[1]) as file_handle:
        content = file_handle.read()
    grid = content.strip().split('\n')

    print(f'read {len(grid)} lines')
    dump_grid(grid)

    tot_rolls = 0
    while True:
        grid_orig = grid.copy()
        num_rolls = 0
        for loc_y in range(0, len(grid_orig)):
            for loc_x in range(0, len(grid_orig[0])):
                if grid_orig[loc_y][loc_x] != '@':
                    continue
                if num_neighbors(grid_orig, loc_y, loc_x) < 4:
                    grid[loc_y] = grid[loc_y][0:loc_x] + 'x' + grid[loc_y][loc_x + 1:]
                    num_rolls += 1
                # print(f'num_neigbors[{loc_y}, {loc_x}]: {num_neighbors(grid, loc_y, loc_x)}')
        dump_grid(grid)
        print(f'Found {num_rolls} rolls')
        tot_rolls += num_rolls
        if num_rolls == 0:
            break
    print(f'Found [{tot_rolls}] rolls total')



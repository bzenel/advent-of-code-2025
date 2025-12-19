import sys
import re
import math
from functools import cmp_to_key
from collections import deque

def dump_matrix(matrix):
    for row in matrix:
        print(row)

if __name__ == "__main__":
    print(f'starting...')

    with open(sys.argv[1]) as file_handle:
        content = file_handle.read()
    lines = content.strip().split('\n')

    print(f'read {len(lines)} lines')

    matrix = lines.copy()

    start_col = matrix[0].index('S')
    print(f'Start is at loc {start_col}')
    matrix[0] = matrix[0][0:start_col] + '|' + matrix[0][start_col+1:]

    print('Matrix:')
    dump_matrix(matrix)

    num_splits = 0
    for row_ind in range(1, len(matrix)):
        for col_ind in range(0, len(matrix[0])):
            curr_char = matrix[row_ind][col_ind]
            above_char = matrix[row_ind-1][col_ind]
            # print(f'curr_char [{curr_char}]')
            if curr_char == '|':
                continue
            if curr_char == '^':
                if above_char == '|':
                    if matrix[row_ind][col_ind-1] != '|':
                        matrix[row_ind] = matrix[row_ind][0:col_ind-1] + '|' + matrix[row_ind][col_ind:]
                    matrix[row_ind] = matrix[row_ind][0:col_ind+1] + '|' + matrix[row_ind][col_ind+2:]
                    num_splits += 1
                    continue
            if above_char == '|':
                matrix[row_ind] = matrix[row_ind][0:col_ind] + '|' + matrix[row_ind][col_ind+1:]

    print('Final matrix:')
    dump_matrix(matrix)
    print(f'Num splits: {num_splits}')

    print('Part 2!')

    matrix = lines.copy()
    matrix[0] = matrix[0][0:start_col] + '|' + matrix[0][start_col+1:]

    print('Matrix:')
    dump_matrix(matrix)

    max_row = len(matrix)
    max_col = len(matrix[0])

    matrix_stack = deque([])
    matrix_stack.appendleft([matrix, 1, 0])
    num_worlds = 1
    while len(matrix_stack) > 0:
        if (len(matrix_stack) % 10000 == 0) or (len(matrix_stack) < 1000):
            print(f'num stacks: {len(matrix_stack)}')
        matrix, row_ind, col_ind = matrix_stack.popleft()
        # print('Incoming matrix')
        # dump_matrix(matrix)
        found_split = False
        while row_ind < max_row:
            while col_ind < max_col:
                curr_char = matrix[row_ind][col_ind]
                above_char = matrix[row_ind-1][col_ind]
                # print(f'curr_char [{curr_char}]')
                if curr_char == '|':
                    pass
                elif curr_char == '^':
                    if above_char == '|':
                        left_char = matrix[row_ind][col_ind-1]
                        matrix[row_ind] = matrix[row_ind][0:col_ind-1] + '|' + matrix[row_ind][col_ind:]
                        matrix_stack.append([matrix.copy(), row_ind+1, 0])
                        matrix[row_ind] = matrix[row_ind][0:col_ind-1] + left_char + matrix[row_ind][col_ind:]    
                        matrix[row_ind] = matrix[row_ind][0:col_ind+1] + '|' + matrix[row_ind][col_ind+2:]
                        matrix_stack.append([matrix.copy(), row_ind+1, 0])
                        num_worlds += 1
                        found_split = True
                        break
                elif above_char == '|':
                    matrix[row_ind] = matrix[row_ind][0:col_ind] + '|' + matrix[row_ind][col_ind+1:]
                col_ind += 1
            if found_split is True:
                break
            col_ind = 0
            row_ind += 1
    print(f'Num worlds: {num_worlds}')

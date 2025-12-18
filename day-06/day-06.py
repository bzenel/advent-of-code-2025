import sys
import re
import math
from functools import cmp_to_key
from collections import deque

def parse_operand_line(line):
    return [int(x) for x in re.findall(r'\d+', line)]

def parse_operator_line(line):
    return re.findall(r'[+\-*/]', line)

if __name__ == "__main__":
    print(f'starting...')

    with open(sys.argv[1]) as file_handle:
        content = file_handle.read()
    lines = content.strip().split('\n')

    print(f'read {len(lines)} lines')

    matrix = []
    for line in lines[0:-1]:
        row_list = parse_operand_line(line)
        print(f'row: {row_list}')
        matrix.append(row_list)
    op_list = parse_operator_line(lines[-1])
    print(f'ops: {op_list}')

    tot_list = []
    for cols in range(0, len(matrix[0])):
        col_total = 0 if op_list[cols] == '+' else 1
        for rows in range(0, len(matrix)):
            if op_list[cols] == '*':
                col_total *= matrix[rows][cols]
            else:
                col_total += matrix[rows][cols]
        tot_list.append(col_total)

    print(f'totals: {tot_list}')
    print(f'big total: {sum(tot_list)}')

    print('Part 2!')

    for cols in range(0, len(matrix[0])):
        col_total = 0 if op_list[cols] == '+' else 1
        operand_list = []
        for rows in range(0, len(matrix)):
            operand_list.append(matrix[rows][cols])
        width = max([len(str(x)) for x in operand_list])
        new_operand_list = []
        for value in operand_list:
            # new_value = str(value) + ("0" if op_list[cols] == '+' else "1") * (width - len(str(value)))
            new_value = " " * (width - len(str(value))) + str(value)
            new_operand_list.append(new_value)
        print(f'operand list: {operand_list}, padded version: {new_operand_list}')
        trans_op_list = []
        for x in range(0, len(new_operand_list[0])):
            trans_op = ""
            for y in range(0, len(new_operand_list)):
                trans_op = trans_op + new_operand_list[y][x]
                print(f'trans_op: [{trans_op}]')
            trans_op_list.append(trans_op)
        print(f'trans op list: {trans_op_list}')

    matrix = lines[0:-1]
    print(f'matrix: {matrix}')
    row_count = 1
    matrix_rot_row = []
    matrix_rot_list = []
    for x in range(0, len(matrix[0])):
        rot_str = ""
        for y in range(0, len(matrix)):
            rot_str = rot_str + matrix[y][x]
            print(f'rot_str: <{rot_str}>')
        if len(rot_str.strip()) > 0:
            matrix_rot_row.append(int(rot_str.strip()))
        else:
            matrix_rot_list.append(matrix_rot_row)
            matrix_rot_row = []
    matrix_rot_list.append(matrix_rot_row)
    print(f'matrix rot list: {matrix_rot_list}')

    tot_list = []
    for row_num in range(0, len(matrix_rot_list)):
        if op_list[row_num] == '*':
            row_total = math.prod(matrix_rot_list[row_num])
        else:
            row_total = sum(matrix_rot_list[row_num])
        tot_list.append(row_total)

    print(f'totals: {tot_list}')
    print(f'big total: {sum(tot_list)}')



    

        
    
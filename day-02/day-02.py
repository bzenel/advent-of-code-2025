import sys

# 1212121212 -- len is 10, 5 sets of 12

def chunk_string(s, n):
    return [s[i:i+n] for i in range(0, len(s), n)]

def is_invalid(num_string: str) -> bool:
    str_len = len(num_string)
    for i in range(1, str_len):
        # print(f'dividing into chunks of size: {i}')
        if str_len % i != 0:
            continue
        chunks = chunk_string(num_string, i)
        # print(f'chunks: {chunks}')
        if len(set(chunks)) == 1:
            return True
    return False

if __name__ == "__main__":
    print(f'starting...')

    with open(sys.argv[1]) as file_handle:
        content = file_handle.read()
    lines = content.strip().split('\n')

    print(f'read {len(lines)} lines')

    ranges = lines[0].split(',')

    for range_val in ranges:
        start, end = range_val.split('-')
        print(f'start: {start}, end: {end}')

    # Brute forcing our way through the ranges
    invalid_sum = 0
    for range_val in ranges:
        start, end = range_val.split('-')
        for i in range(int(start), int(end)+1):
            num_string = f'{i}'
            if len(num_string) % 2 == 1:
                continue
            # print(f'num_string: {num_string}')
            left_half = num_string[0:len(num_string)//2]
            right_half = num_string[len(num_string)//2:]
            if left_half == right_half:
                print(f'left_half: {left_half}, right_half: {right_half}')
                invalid_sum += i
    print(f'invalid_sum: {invalid_sum}')

    ### Part 2

    invalid_sum = 0
    for range_val in ranges:
        start, end = range_val.split('-')
        for i in range(int(start), int(end)+1):
            if is_invalid(f'{i}'):
                print(f'invalid: {i}')
                invalid_sum += i
    print(f'invalid_sum: {invalid_sum}')
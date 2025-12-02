import sys

if __name__ == "__main__":
    print(f'starting...')

    with open(sys.argv[1]) as file_handle:
        content = file_handle.read()
    lines = content.strip().split('\n')

    print(f'read {len(lines)} lines')

    position = 50
    zeros_count = 0
    for line in lines:
        direction = line[0]
        distance = int(line[1:])
        delta = distance * (1 if direction == 'R' else -1)
        position = (position + delta) % 100
        print(f'direction: {direction}, distance: {distance}, position: {position}')
        if position == 0:
            zeros_count += 1
    print(f'zeros_count: {zeros_count}')

    print('Part 2')
    position = 50
    zeros_count = 0
    for line in lines:
        direction = line[0]
        distance = int(line[1:])
        rotations = distance // 100
        distance -= rotations * 100
        zeros_count += rotations
        delta = distance * (1 if direction == 'R' else -1)
        if position == 0:
            position += delta
        else:
            position += delta
            if position < 0 or position > 100:
                zeros_count += 1
        position = position % 100
        print(f'direction: {direction}, distance: {distance}, position: {position}')
        if position == 0:
            zeros_count += 1
    print(f'zeros_count: {zeros_count}')
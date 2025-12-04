import sys

if __name__ == "__main__":
    print(f'starting...')

    with open(sys.argv[1]) as file_handle:
        content = file_handle.read()
    lines = content.strip().split('\n')

    print(f'read {len(lines)} lines')

    tot_joltage = 0
    for bank in lines:
        print(f'bank: {bank}')
        first_digit = max(bank)
        location = bank.index(first_digit)
        if location == len(bank) - 1:
            second_digit = first_digit
            bank = bank[0:location]
            print(f'bank updated: {bank}')
            first_digit = max(bank)
        else:
            second_digit = max(bank[location+1:])
        print(f'first_digit: {first_digit}, second_digit: {second_digit}')
        tot_joltage += int(f'{first_digit}{second_digit}')
    print(f'tot_joltage: {tot_joltage}')

    print('Part 2')
    tot_joltage = 0
    bank_len = len(lines[0])
    for bank in lines:
        print(f'bank: {bank}')
        battery_list = ''
        chunk_len = bank_len - 12 + 1
        while len(battery_list) < 12:
            print(f'bank: {bank}, chunk_len: {chunk_len}, {max(bank[0:chunk_len])}')
            digit = max(bank[0:chunk_len])
            battery_list += f'{digit}'
            location = bank.index(digit)
            bank = bank[location+1:]
            chunk_len = chunk_len - location
            print(f'battery: {battery_list}, new bank: {bank}')
        tot_joltage += int(battery_list)
    print(f'total joltage: {tot_joltage}')



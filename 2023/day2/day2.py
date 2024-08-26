import re

MAX_RED = 12
MAX_GREEN = 13
MAX_BLUE = 14

def read_data_from_file(file):
    data = []
    with open(file, 'r') as f:
        data = f.read().split('\n')
    return data

def parse_line(line):
    id = int(line.split(':')[0].strip('Game '))
    rolls = re.findall('([0-9]+ [rgb])', line)
    for roll in rolls:
        if not is_possible(roll):
            return False
    return id

def is_possible(str):
    val = int(str.split(' ')[0].strip())
    if 'r' in str and val > MAX_RED:
        return False
    if 'g' in str and val > MAX_GREEN:
        return False
    if 'b' in str and val > MAX_BLUE:
        return False
    return True

if __name__ == '__main__':
    data = read_data_from_file('input.txt')
    total = 0
    for line in data:
        val = parse_line(line)
        if val:
            total += val
    print(total)
        
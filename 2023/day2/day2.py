import re

MAX_RED = 12
MAX_GREEN = 13
MAX_BLUE = 14

def read_data_from_file(file):
    data = []
    with open(file, 'r') as f:
        data = f.read().split('\n')
    return data

def get_min(line):
    id = int(line.split(':')[0].strip('Game '))
    rolls = re.findall('([0-9]+ [rgb])', line)
    min_r = 0
    min_g = 0
    min_b = 0
    for roll in rolls:
        vals = get_values(roll)
        if vals[1] == 'r' and vals[0] > min_r:
            min_r = vals[0]
        if vals[1] == 'g' and vals[0] > min_g:
            min_g = vals[0]
        if vals[1] == 'b' and vals[0] > min_b:
            min_b = vals[0]
    print(min_r, min_g, min_b)
    return min_r, min_g, min_b
        
def get_values(str):
    val = int(str.split(' ')[0].strip())
    return val, str.split(' ')[1].strip()

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
        vals = get_min(line)
        total = total + (vals[0] * vals[1] * vals[2])
    print(total)
        
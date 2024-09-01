import re
from re import finditer

def read_data():
    lines = []
    with open('input.txt', 'r') as f:
        lines = f.read().split('\n')
    return lines

def check_box(lines):
    sum = 0
    last_n = 0
    for i, line in enumerate(lines):
        for match in re.finditer('([0-9])+', line):
            span = match.span()
            mat = match.group()
            is_valid = False
            left = span[0] - 1 if span[0] > 0 else span[0]
            right = span[1] + 1 if span[1] < len(line) else span[1]
            prev = lines[i-1][left:right] if i > 0 else ''
            curr = lines[i][left:right]
            next = lines[i+1][left:right] if i < len(lines) else ''
            if re.search('[^0-9.]', prev) or re.search('[^0-9.]', curr) or re.search('[^0-9.]', next):
                is_valid = True
            print(is_valid, mat)
#           print(prev)
#           print(curr)
#           print(next, is_valid)
            if is_valid:
                sum += int(mat)
            if last_n == mat:
                print(mat)
            last_n = mat
    return sum

if __name__ == '__main__':
    data = read_data()
    sum = check_box(data)
    print(sum)


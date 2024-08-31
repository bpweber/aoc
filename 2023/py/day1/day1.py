digits = [
    '1',
    '2',
    '3',
    '4',
    '5',
    '6',
    '7',
    '8',
    '9',
    'one',
    'two',
    'three',
    'four',
    'five',
    'six',
    'seven',
    'eight',
    'nine',
]

digit_maps = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9'
}

def find_digitloc_in_line(line):
    first = [999, '']
    last = [-1, '']
    for d in digits:
        lloc = line.find(d)
        rloc = line.rfind(d)
        if lloc != -1 and lloc < first[0]:
            first = lloc, d
        if rloc > last[0]:
            last = rloc, d
#    print(first, last)
    if not first[1].isdigit():
        first = digit_maps[first[1]]
    else:
        first = first[1]
    if not last[1].isdigit():
        last = digit_maps[last[1]]
    else:
        last = last[1]
#    print(first + last)
    return first + last

def read_input_from_file(file):
    with open(file) as f:
        input = f.read().split('\n')
        print(input)
        return(input)

def get_calibration_value_from_line(line):
    sum = ''
    for char in line:
        if char.isdigit():
            sum += char
            break
    for char in reversed(line):
        if char.isdigit():
            sum += char
            break
    print(sum)
    return(sum)

if __name__ == '__main__':
    input = read_input_from_file('input.txt')
#    print(find_digitloc_in_line('sdpgz3five4seven6fiveh'))
    sum = 0
    for i, line in enumerate(input):
        val = int(find_digitloc_in_line(line))
        print(i+1, val)
        sum += val
    print(sum)

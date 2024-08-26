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

input = read_input_from_file('input.txt')

sum = 0
for line in input:
    val = int(get_calibration_value_from_line(line))
    sum += val
print(sum)

with open('2.in', 'r') as f:
    orig_data = list(map(int, f.read().strip().split(",")))


def intcode(data, input_1, input_2):
    data = data.copy()
    data[1] = input_1
    data[2] = input_2
    pointer = 0
    while True:
        instr, ptr_1, ptr_2, ptr_3 = data[pointer:pointer + 4]
        if instr == 1:
            data[ptr_3] = data[ptr_1] + data[ptr_2]
        elif instr == 2:
            data[ptr_3] = data[ptr_1] * data[ptr_2]
        elif instr == 99:
            return data
        else:
            raise ValueError(f"instr {instr}")
        pointer += 4


# Part 1
data1 = intcode(orig_data, 12, 2)
print(data1[0])


# Part 2
def part2():
    for noun in range(100):
        for verb in range(100):
            data = intcode(orig_data, noun, verb)
            if data[0] == 19690720:  # Magic number
                return 100 * noun + verb


print(part2())

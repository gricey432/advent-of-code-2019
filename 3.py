from collections import defaultdict


with open('3.in', 'r') as f:
    orig_data = [
        [
            (instr[0], int(instr[1:]))
            for instr in line.strip().split(",")
        ]
        for line in f
    ]


# Part 1
def p1():
    coords = defaultdict(set)
    for line_n, line in enumerate(orig_data):
        x = 0
        y = 0
        for instr, length in line:
            for i in range(length):
                if instr == "U":
                    y += 1
                elif instr == "D":
                    y -= 1
                elif instr == "R":
                    x += 1
                elif instr == "L":
                    x -= 1
                else:
                    raise ValueError()
                coords[(x, y)].add(line_n)

    return sorted(
        abs(x) + abs(y)
        for (x, y), c in coords.items()
        if len(c) > 1
    )[0]


print(p1())


# Part 2
def p2():
    coords = defaultdict(lambda: [None] * len(orig_data))
    for line_n, line in enumerate(orig_data):
        x = 0
        y = 0
        c = 0
        for instr, length in line:
            for i in range(length):
                if instr == "U":
                    y += 1
                elif instr == "D":
                    y -= 1
                elif instr == "R":
                    x += 1
                elif instr == "L":
                    x -= 1
                else:
                    raise ValueError()
                c += 1
                curval = coords[(x, y)][line_n]
                if curval is None or c < curval:
                    coords[(x, y)][line_n] = c

    return sorted(
        sum(v)
        for v in coords.values()
        if None not in v
    )[0]


print(p2())

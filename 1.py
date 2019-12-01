with open('1.in', 'r') as f:
    data = list(map(int, f))


# Part 1
print(sum(
    v // 3 - 2
    for v in data
))


# Part 2
def rec_fuel(weight):
    fuel = weight // 3 - 2
    if fuel < 1:
        return 0
    return fuel + rec_fuel(fuel)


print(sum(
    v // 3 - 2 + rec_fuel(v // 3 - 2)  # Assignment expression would be nice here
    for v in data
))

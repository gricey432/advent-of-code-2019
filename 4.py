# Puzzle input
lower = 109165
upper = 576723


# Part 1
def test1(n):
    digits = [n // (10 ** i) % 10 for i in range(5, -1, -1)]

    # Never decreasing
    for i in range(5):
        if digits[i] > digits[i + 1]:
            return False

    # Double digit
    for i in range(5):
        if digits[i] == digits[i+1]:
            break
    else:
        return False

    return True


print(sum(
    1 for n in range(lower, upper + 1)
    if test1(n)
))


# Part 2
def test2(n):
    digits = [n // (10 ** i) % 10 for i in range(5, -1, -1)]

    # Never decreasing
    for i in range(5):
        if digits[i] > digits[i + 1]:
            return False

    # Double digit but not part of a larger sequence
    for i in range(5):
        if (
            (i == 0 or digits[i-1] != digits[i])
            and digits[i] == digits[i+1]
            and (i == 4 or digits[i+1] != digits[i+2])
        ):
            break
    else:
        return False

    return True


print(sum(
    1 for n in range(lower, upper + 1)
    if test2(n)
))

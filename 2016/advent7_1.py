def is_abba(sign1, sign2, sign3, sign4):
    return sign1 == sign4 and sign2 == sign3 and sign1 != sign2


def has_abba(line):
    for i in range(0, len(line) - 3):
        if is_abba(line[i], line[i + 1], line[i + 2], line[i + 3]):
            return True
    return False


with open("input7.txt", 'r') as inputFile:
    lines = inputFile.read().splitlines()
    sum = 0
    for line in lines:
        firstSplit = line.split('[')
        hypernetSequences = filter(None,
                                   list(None if i == 0 else item.split(']')[0] for i, item in enumerate(firstSplit)))
        supernetSequences = list(item if i == 0 else item.split(']')[1] for i, item in enumerate(firstSplit))

        if (any(has_abba(item) for item in supernetSequences)) and not any(has_abba(item) for item in hypernetSequences):
            sum += 1
    print sum

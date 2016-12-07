def is_xyx(sign1, sign2, sign3):
    return sign1 == sign3 and sign1 != sign2


def is_corresponding(xyx, aba):
    return xyx[0] == aba[1] and xyx[1] == aba[0]


def has_corresponding_bab(sequence_xyx, aba):
    return any(is_corresponding(xyx, aba) for xyx in sequence_xyx)


def get_all_xyx(line):
    result = []
    for i in range(0, len(line) - 2):
        if is_xyx(line[i], line[i + 1], line[i + 2]):
            result.append(line[i] + line[i + 1] + line[i + 2])
    return result


with open("input7.txt", 'r') as inputFile:
    lines = inputFile.read().splitlines()
    sum = 0
    for line in lines:
        firstSplit = line.split('[')
        hypernetSequences = filter(None,
                                   list(None if i == 0 else item.split(']')[0] for i, item in enumerate(firstSplit)))
        supernetSequences = list(item if i == 0 else item.split(']')[1] for i, item in enumerate(firstSplit))

        supernetSequences_xyx = list(i for item in supernetSequences for i in get_all_xyx(item))
        hypernetSequences_zcz = list(i for item in hypernetSequences for i in get_all_xyx(item))

        if any(has_corresponding_bab(hypernetSequences_zcz, xyx) for xyx in supernetSequences_xyx):
            sum += 1

    print sum

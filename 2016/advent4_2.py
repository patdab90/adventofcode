inputFile = open("input4.txt", 'r')
lines = inputFile.readlines()
inputFile.close()

key = 'abcdefghijklmnopqrstuvwxyz'


def decode(text, n):
    result = ''
    for l in text:
        try:
            result += key[(key.index(l) + n) % len(key)]
        except ValueError:
            result += l
    return result


for line in lines:
    name = line[:line.rfind('-')].replace('-', ' ')
    id = int(line[line.rfind('-') + 1:line.find('[')])
    name = decode(name, id)
    if 'north' in name:
        print name, id

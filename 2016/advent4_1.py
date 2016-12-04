from collections import Counter

inputFile = open("input4.txt", 'r')
lines = inputFile.readlines()
inputFile.close()

sum = 0

for line in lines:
    checkSum = line[line.find('[') + 1:line.rfind(']')]
    name = line[:line.rfind('-')].replace('-', '')
    id = int(line[line.rfind('-')+1:line.find('[')])
    counts = Counter(name)
    name = sorted(counts, key=lambda word: (-counts[word], word))
    sum += id if checkSum == ''.join(name[:5]) else 0

print sum
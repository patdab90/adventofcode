import operator

f = open("input6.txt", 'r')
lines = f.read().splitlines()
f.close()

resultMap = [{} for i in lines[0]]
for line in lines:
    for letter, d in zip(line, resultMap):
        d[letter] = d.get(letter, 0) + 1

print ''.join(list(max(element.iteritems(), key=operator.itemgetter(1))[0] for element in resultMap))

import md5
input = 'reyedfim'

result = ''
i = 0
while len(result) < 8:
    m = md5.new()
    m.update(input + str(i))
    hash = str(m.hexdigest())
    if hash.startswith('00000'):
        result += hash[5]
    i += 1
print result
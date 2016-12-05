import md5
input = 'reyedfim'

result = ['_']*8
i = 0
while '_' in result:
    m = md5.new()
    m.update(input + str(i))
    hash = str(m.hexdigest())
    if hash.startswith('00000'):
        position = hash[5]
        if hash[5].isdigit() and 0 <= int(position) <= 7 and result[int(position)] == '_':
            result[int(position)] = hash[6]
    i += 1
print ''.join(result)
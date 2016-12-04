inputFile = open("input3.txt", 'r')
lines = inputFile.readlines()
inputFile.close()


def is_triangle(a, b, c):
    return (a + b > c) and (b + c > a) and (a + c > b)

triangles = list(map(lambda x: int(x.strip()), line.split()) for line in lines)

result = 0
for t in triangles:
    result += 1 if is_triangle(t[0], t[1], t[2]) else 0


print result

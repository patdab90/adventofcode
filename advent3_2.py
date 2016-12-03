inputFile = open("input.txt", 'r')
fileContent = inputFile.read()
inputFile.close()


def is_triangle(a, b, c):
    return (a + b > c) and (b + c > a) and (a + c > b)

numbers = list(map(lambda x: int(x.strip()), fileContent.split()))

print len(numbers)/3

result = 0
for i in range(0, len(numbers), 9):
    result += 1 if is_triangle(numbers[i  ], numbers[i+3], numbers[i+6]) else 0
    result += 1 if is_triangle(numbers[i+1], numbers[i+4], numbers[i+7]) else 0
    result += 1 if is_triangle(numbers[i+2], numbers[i+5], numbers[i+8]) else 0

print result

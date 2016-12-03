

i = "R1, R3, L2, L5, L2, L1, R3, L4, R2, L2, L4, R2, L1, R1, L2, R3, L1, L4, R2, L5, R3, R4, L1, R2, L1, R3, L4, R5, L4, L5, R5, L3, R2, L3, L3, R1, R3, L4, R2, R5, L4, R1, L1, L1, R5, L2, R1, L2, R188, L5, L3, R5, R1, L2, L4, R3, R5, L3, R3, R45, L4, R4, R72, R2, R3, L1, R1, L1, L1, R192, L1, L1, L1, L4, R1, L2, L5, L3, R5, L3, R3, L4, L3, R1, R4, L2, R2, R3, L5, R3, L1, R1, R4, L2, L3, R1, R3, L4, L3, L4, L2, L2, R1, R3, L5, L1, R4, R2, L4, L1, R3, R3, R1, L5, L2, R4, R4, R2, R1, R5, R5, L4, L1, R5, R3, R4, R5, R3, L1, L2, L4, R1, R4, R5, L2, L3, R4, L4, R2, L2, L4, L2, R5, R1, R4, R3, R5, L4, L4, L5, L5, R3, R4, L1, L3, R2, L2, R1, L3, L5, R5, R5, R3, L4, L2, R4, R5, R1, R4, L3"
ia = i.split(", ")

resultcoords = (0, 0)
N = (1, 0)
S = (-1, 0)
E = (0, 1)
W = (0, -1)
context = N


def calc_movment(forward, coords):
    return tuple(coords[i] + context[i] * forward for i in range(len(coords)))


for action in ia:
    if action[0] == 'R':
        resultcoords = calc_movment(int(action[1:]), resultcoords)
        if context == N:
            context = E
        else:
            if context == S:
                context = W
            else:
                if context == E:
                    context = S
                else:
                    if context == W:
                        context = N
    if action[0] == 'L':
        resultcoords = calc_movment(-int(action[1:]), resultcoords)
        if context == N:
            context = W
        else:
            if context == S:
                context = E
            else:
                if context == E:
                    context = N
                else:
                    if context == W:
                        context = S

print abs(resultcoords[0]) + abs(resultcoords[1])
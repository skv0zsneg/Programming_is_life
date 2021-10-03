import bisect


HAYSRACK = [1, 3, 5, 7, 9, 10, 150, 170, 900]
NEEDLES = [0, 1, 2, 23, 45, 1000]

print(*HAYSRACK, sep='\t')
for needle in reversed(NEEDLES):
    position = bisect.bisect(HAYSRACK, needle)
    offset = '\t |' * position
    print(f"{offset}{needle}")


def grade(score, breakpoints=[60, 70, 80, 90], grades=['FDCBA']):
    i = bisect.bisect(breakpoints, score)
    return grades[i]


"""
    bisect (bisect_right)
        поиск позиции в последовательности справа от элемента, равного искомому.

    bisect_left
        поиск позиции в последовательности слева от элемента, равного искомому.
"""



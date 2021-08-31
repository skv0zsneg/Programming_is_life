from random import choice
"""
    choice -- это выбор случайного элемента из последовательности.
"""

res = choice([1, {'oh': 'my'}, 'GoD!'])

print(res)  # 1 or {'oh': 'my'} or GoD!



from random import shuffle
"""
    shuffle -- это перемешивание изменяемой последовательности.
"""

seq = [1, 2, 3]
shuffle(seq)  # Последовательность перемешивается на месте, возвращается None.

print(seq)  # [1, 2, 3] or [2, 1, 3] or [3, 2, 1] e.c.t.
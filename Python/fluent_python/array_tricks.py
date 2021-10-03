"""
    Наглядный пример сравнения скорости работы array.array и list[int].

    Задача: записать в бинарный файл 10 миллионов случайно полученных строк.
    Полученные значения.
    array:      chrs = 106, ..., 66
    array:      Time: 0.04505610000000004
    list[int]:  lst = 106, ..., 66
    list[int]:  Time: 3.0652329
"""
import random
import string
import functools
from array import array
from time import perf_counter as pc


def check_speed(f):
    @functools.wraps(f)
    def inner(*args, **kwargs):
        t0 = pc()
        res =  f(*args, **kwargs)
        print(f"Time: {pc() - t0}")
        return res
    
    return inner


RANDOM_STRING = ''.join(random.choice(string.ascii_letters) for _ in range(10**7))
print(f"RANDOM_STRING = {RANDOM_STRING[0]}, ..., {RANDOM_STRING[-1]}")
ENCODED_RANDOM_STRING = RANDOM_STRING.encode()


@check_speed
def work_with_array():
    chrs = array('b', ENCODED_RANDOM_STRING)
    print(f"chrs = {chrs[0]}, ..., {chrs[-1]}")
    with open('file.bin', 'wb') as fd:
        chrs.tofile(fd)


@check_speed
def work_with_list():
    lst = [i for i in ENCODED_RANDOM_STRING]
    print(f"lst = {lst[0]}, ..., {lst[-1]}")
    with open('file.bin', 'wb') as fd:
        for el in lst:
            fd.write(el.to_bytes(24, 'big'))


if __name__ == "__main__":
    work_with_array()
    work_with_list()
from random import choice
from collections import deque
from string import ascii_letters
from time import perf_counter as pc


dq = deque('iterable object', maxlen=10)
print(dq)  # deque(['b', 'l', 'e', ' ', 'o', 'b', 'j', 'e', 'c', 't'], maxlen=10)

dq.rotate(5)
print(dq)  # deque(['b', 'j', 'e', 'c', 't', 'b', 'l', 'e', ' ', 'o'], maxlen=10)

dq.rotate(-6)
print(dq)  # deque(['l', 'e', ' ', 'o', 'b', 'j', 'e', 'c', 't', 'b'], maxlen=10)

dq.appendleft(-1) 
print(dq)  # deque([-1, 'l', 'e', ' ', 'o', 'b', 'j', 'e', 'c', 't'], maxlen=10)

dq.extend(['w', 't', 'f'])
print(dq)  # deque([' ', 'o', 'b', 'j', 'e', 'c', 't', 'w', 't', 'f'], maxlen=10)

dq.extendleft(['g', 'm', 'o'])
print(dq)  # deque(['o', 'm', 'g', ' ', 'o', 'b', 'j', 'e', 'c', 't'], maxlen=10)

from types import MappingProxyType

"""
    MappingProxyType позволяет в динамике наблюдать изменение mapping объекта,
    без возможности (через mappingproxy) изменять сам объект.
"""
d = {1: 'one', 2: 'two'}
prx_d = MappingProxyType(d)
print(prx_d)  # {1: 'one', 2: 'two'}

try:
    prx_d[1] = 'ONE'
except TypeError as e:
    print(e)  # 'mappingproxy' object does not support item assignment

d.update({3: 'three'})
print(prx_d)  # {1: 'one', 2: 'two', 3: 'three'}

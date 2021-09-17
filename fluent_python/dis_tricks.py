"""
    dis - дизассемблер для Python байткода.
    
    Документация (ru): https://digitology.tech/docs/python_3/library/dis.html
"""
from dis import dis 

def foo(n):
    len(n)

print(dis(foo))
"""
  7           0 LOAD_GLOBAL              0 (len)
              2 LOAD_FAST                0 (n)
              4 CALL_FUNCTION            1
              6 POP_TOP
              8 LOAD_CONST               0 (None)
             10 RETURN_VALUE
"""

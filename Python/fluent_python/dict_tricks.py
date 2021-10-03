from typing import DefaultDict


"""
    Примеры создания словаря.
"""
a = dict(one=1, two=2, three=3)  # Как в **kwargs ф-ции
b = {'one': 1, 'two': 2, 'three': 3}  # Тело словаря 
c = dict(zip(['one', 'two', 'three'], (1, 2, 3)))  # "Склеивание" zip-ом
d = dict([('one', 1), ('two', 2), ('three', 3)])  # Список кортежей
e = dict({'three': 3, 'one': 1, 'two': 2})  # Последовательность не важна

print(a == b == c == d == e)  # True


"""
    Словарное включение: dcitcomp
"""
CODES = {
    (1, 'one'),
    (2, 'two'),
    (3, 'three')
}

get_codes = {str_code: int_code for int_code, str_code in CODES}
print(get_codes)  # {'one': 1, 'two': 2, 'three': 3}
reversed_codes = {int_code: str_code.upper() for str_code, int_code in get_codes.items()}
print(reversed_codes)  # {3: 'THREE', 1: 'ONE', 2: 'TWO'}


"""
    Еще всякое:
"""
d = dict()
d.update([(1, 'one'), (2, 'two'), (3, 'three')])  # Обновление словаря списком кортежей
print(d)  # {1: 'one', 2: 'two', 3: 'three'}

d = {1: 'one', 2: 'two', 3: 'three'}
res = d.setdefault('four', 4)   # Вернуть значение из словаря по ключу, если оно есть. 
                                # Иначе создать пару ключ значение с __default значением.
print(res)  # 4
print(d)  # {1: 'one', 2: 'two', 3: 'three', 'four': 4}

d = {1: 'one', 2: 'two', 3: 'three'}
res = d.get('four', None)  # Вернуть значение из словаря по ключу, если оно есть. 
                        # Иначе вернуть значение default (вместо KeyError).
print(res)  # None
print(d)  # {1: 'one', 2: 'two', 3: 'three'}
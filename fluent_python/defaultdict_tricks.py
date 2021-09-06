from collections import defaultdict


"""
    В defaultdict используется специальный метод __missing__.
"""

dd = defaultdict(list)
KEY = 'mmm'
print(dd[KEY])  # Если значения в словаре dd по ключу KEY нет, создается запись в словаре dd со значением [].
print(dd.get(KEY))  # Поиск через get успешен, т.к. выше создалась такая запись.
print(dd.get('?')) # Поиск провален, т.к. запись с ключом '?' не создана.

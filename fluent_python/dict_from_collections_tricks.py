from collections import defaultdict, OrderedDict, ChainMap, Counter, UserDict


"""
    В defaultdict используется специальный метод __missing__.
"""
dd = defaultdict(list)
KEY = 'mmm'
print(dd[KEY])  # Если значения в словаре dd по ключу KEY нет, создается запись в словаре dd со значением [].
print(dd.get(KEY))  # Поиск через get успешен, т.к. выше создалась такая запись.
print(dd.get('?')) # Поиск провален, т.к. запись с ключом '?' не создана.


"""
    OrderedDict - отображение, в котором ключи хранятся так же как и задавались. 
    Гарантируя фиксированную последовательность.
"""
od = OrderedDict(one=1, two=2, three=3)
print(od)  # OrderedDict([('one', 1), ('two', 2), ('three', 3)])
print(od['one'], od['three'])  # 1 3
# .popitem(last=Union[True, False]) Удаляет и возвращает первый элемент из последовательности, если last=True. 
# И последний, если last=False.
print(od.popitem(last=True))  # ('three', 3)
print(od.popitem(last=False))  # ('one', 1)


"""
    ChainMap - хранение нескольких словарей в одном инстансе для одновременного 
    доступа ко всем из них, через объект, как к одному.
"""
cm = ChainMap({'one': 1}, {'a': 'A'}, {'42': 21})
print(cm['one'], cm['42'], cm['a'])  # 1 21 A
print([(k, v) for k, v in cm.items()])  # [('42', 21), ('a', 'A'), ('one', 1)]


"""
    Counter - отображение, в котором с каждым ключом ассоциирован счетчик. 
    Принемает итерируемый объект.
"""
c = Counter('123123123abcabcABCABC')
print(c)  # Counter({'1': 3, '2': 3, '3': 3, 'a': 2, 'b': 2, 'c': 2, 'A': 2, 'B': 2, 'C': 2})
c.update((1, 2, 3, 4))
print(c)  # Counter({'1': 3, '2': 3, '3': 3, 'a': 2, 'b': 2, 'c': 2, 'A': 2, 'B': 2, 'C': 2, 1: 1, 2: 1, 3: 1, 4: 1})


"""
    UserDict - класс, позволяющий определять пользовательский dict, не переопределяя методы самого dict.
"""
class StrKeyDict(UserDict):
    """Класс позволяет получать значения по ключу, 
    который хранится как str, но который пытаются получить через int.
    Например:
        >>> d = StrKeyDict({'1': 'one', '2': 'two', 3: 'three'})
        >>> d[1]
        one
        >>> d['3']
        three
    """
    def __missing__(self, key: object):  # метод вызывается при отсутствии значения по ключу в self.data.
        if isinstance(key, str):
            raise KeyError(key)
        return self[str(key)]
    
    def __contains__(self, key: object):
        return str(key) in self.data  # self.data - экзэмпляр dict в UserDict.

    def __setitem__(self, key, item):
        self.data[str(key)] = item

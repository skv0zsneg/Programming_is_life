from collections import UserDict


class MySum:
    def __init__(self, *args) -> None:
        self._args = args
        self.res = sum(args)
    
    def __getitem__(self, key) -> int:
        """Магический метод __getitem__ 'получает' значение по ключу key, 
        при обращении к экземпляру класса через синтаксическую 
        конструкцию obj[key]."""
        return self._args[key]
    
    def __str__(self) -> str:
        """Магический метод __str__ выводит ЧИТАЕМОЕ строковое представления объекта класса."""  
        r = str(self._args[0])
        for el in self._args[1:]:
            r += f' + {el}'
        return f"{r} = {self.res}"
    
    def __repr__(self) -> str:
        """Магический метод __repr__ выводит строковое представление объекта класса
        МАКСИМАЛЬНО ПРИБЛИЖЕННОЕ К СИНТАКСИСУ языка Python."""
        return f"MySum({', '.join(str(v) for v in self._args)})"


res = MySum(2, 3, 4, 5, 7, 1000)
print(repr(res))  # 2 + 3 + 4 + 5 + 7 + 1000 = 1021
print(res)  # MySum(2, 3, 4, 5, 7, 1000)
print(res[3])  # 5


"""
    __missing__ объект вызывается только тогда, когда при обращении 
    к __getitem__(self, k) искомое значение не было найдено.
"""
class MyDict(UserDict):
    def __missing__(self, k):
        return None

d = MyDict(one=1, two=2, three=3)
print(d['four'])  # None

# __repr__
class MySum:
    def __init__(self, *args) -> None:
        self._args = args
        self.res = sum(args)

    def __repr__(self) -> str:
        """Магический метод __repr__ выводит строковое представления объекта класса."""  
        r = str(self._args[0])
        for el in self._args[1:]:
            r += f' + {el}'
        return f"{r} = {self.res}"


res = MySum(2)
print(res)


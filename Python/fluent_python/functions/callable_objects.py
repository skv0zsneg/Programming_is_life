"""Благодаря магическому методу __call__ можно сохранить некое состояние 
объекта и возвращаться к нему. При этом экземпляр класса будет симулировать 
функцию."""


class CallableClass(object):
    def __init__(self, start: int = 0) -> None:
        self.val = start

    def increase(self):
        self.val += 1
    
    def __call__(self):
        self.increase()


class NotCallableClass(object):
    def __init__(self) -> None:
        pass


counter = CallableClass()
non_call = NotCallableClass()

counter.increase()
print(counter.val)
# 1

counter()
print(counter.val)
# 2

# callable проверяем является ли объект вызываемым.
print(callable(counter))
# True

print(callable(non_call))
# False
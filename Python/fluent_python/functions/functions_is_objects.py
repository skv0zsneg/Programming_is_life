"""Функции являются объектами наз. полноправными со всеми вытекающими 
свойствами полноправных объектов."""


def func(*args, **kwagrs) -> None:
    print(args, kwagrs)


func('say hi', my='Love')
# ('say hi',) {'my': 'Love'}
name = func
name('say hi', my='Love')
# ('say hi',) {'my': 'Love'}
print(type(name) == type(func))
# True
print(type(name) is type(func))
# True
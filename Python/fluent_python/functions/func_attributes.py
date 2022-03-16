"""У функций помимо __doc__ есть куча иных атрибутов."""


class C:
    pass


inst = C()


def print_everything(default=1, *args, kwdefaults='2', **kwargs) -> None:
    print(args, kwargs)


# Вычисление атрибутов существующих только для функций
f_atrs = sorted(set(dir(print_everything)) - set(dir(inst)))
print(f_atrs)
# ['__annotations__', '__call__', '__closure__', '__code__', '__defaults__', 
# '__get__', '__globals__', '__kwdefaults__', '__name__', '__qualname__']


print(print_everything.__annotations__)  # Аннотация параметров и возвращаемого значения
# {'return': None}

print(print_everything.__call__)  # Реализация оператоа `()` (метод)
# <method-wrapper '__call__' of function object at 0x000001612E7FF040>

print(print_everything.__closure__)  # Замыканий ф-ций т.е. привязки свободных аргументов [c. 179]
# None

print(print_everything.__code__)  # Метаданные и тело ф-ции откомпилированные в байт код
# <code object print_everything at 0x000001612E800240, file "...\fluent_python\functions\func_attributes.py", line 11>

print(print_everything.__defaults__)  # Значения формальных параметров по умолчанию [c. 179]
# (1,)

print(print_everything.__get__)  # Рализация протокола дискриптора (метод)
# <method-wrapper '__get__' of function object at 0x000001DCD113F040>

print(print_everything.__globals__)  # Глобальные аргументы модуля, в котором определена ф-ция
# {'__name__': '__main__', '__doc__': 'У функций помимо __doc__ есть куча иных атрибутов.', '__package__': None, 
# '__loader__': <_frozen_importlib_external.SourceFileLoader object at 0x000001DCD106A100>, '__spec__': None, 
# '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>, 
# '__file__': '...\\fluent_python\\functions\\func_attributes.py', 
# '__cached__': None, 'C': <class '__main__.C'>, 'inst': <__main__.C object at 0x000001DCD1147FD0>, 
# 'print_everything': <function print_everything at 0x000001DCD113F040>, 
# 'f_atrs': ['__annotations__', '__call__', '__closure__', '__code__', '__defaults__', '__get__', 
# '__globals__', '__kwdefaults__', '__name__', '__qualname__']}


print(print_everything.__kwdefaults__)  # Значения по умолчанию формальных чисто именованных аргументов [c. 179] 
# {'kwdefaults': '2'}

print(print_everything.__name__)  # Имя ф-ции
# print_everything

print(print_everything.__qualname__)  # Полное имя (с модулем) до ф-ции 
# print_everything


"""Если необходимо исследовать сигнатуру ф-ции можно воспользоваться методом 
signature из модуля inspect"""

from inspect import signature


sig = signature(print_everything)
for name, param in sig.parameters.items():
    print(param.kind, ':', name, '=', param.default)
    # POSITIONAL_OR_KEYWORD : default = 1
    # VAR_POSITIONAL : args = <class 'inspect._empty'>
    # KEYWORD_ONLY : kwdefaults = 2
    # VAR_KEYWORD : kwargs = <class 'inspect._empty'>

# <class 'inspect._empty'> обозначает не указанное значение по умолчанию.


# Можно переписывать словарь аргументов sig с помощью метода bind
d = {'default': 2, 'new': 3, 'kwdefaults': 4, 'kwnew': 5}
bound_args = sig.bind(**d)
for name, value in bound_args.arguments.items():
    print(name, '=', value)
    # default = 2
    # kwdefaults = 4
    # kwargs = {'new': 3, 'kwnew': 5}
